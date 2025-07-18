#    This program handles the creation of Casbin policies for database authentication.
#    Copyright (C) 2025, The CS Nerds (HippoProgrammer & SuitablyMysterious)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
import logging
import sys
import os
from casbin import Enforcer, persist
from casbin_sqlalchemy_adapter import Adapter
from sqlalchemy import create_engine

log = logging.getLogger(__name__)
log_handler = logging.StreamHandler(sys.stdout)

log.addHandler(log_handler)
log.setLevel(logging.INFO)

log.info('Initiating policySetup.py')

MODEL_PATH   = Path(__file__).parent / "model.conf"
POLICY_PATH = Path(__file__).parent / "policy.csv"

DSN = f"postgresql+psycopg://{"casbin_login"}:{os.environ["CASBIN_LOGIN_PASS"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}"

engine  = create_engine(DSN, future=True)
adapter = Adapter(engine)

enforcer = Enforcer(str(MODEL_PATH), adapter, auto_save=False)
enforcer.load_policy()
db_enforcer = Enforcer(str(MODEL_PATH), adapter, auto_save=False)
file_enforcer = Enforcer(str(MODEL_PATH), str(POLICY_PATH))

for rule in file_enforcer.get_policy():
    if not db_enforcer.has_policy(*rule):
        db_enforcer.add_policy(*rule)
for link in file_enforcer.get_named_grouping_policy():
    if not db_enforcer.has_grouping_policy(*link):
        db_enforcer.add_grouping_policy(*link)

log.info('policySetup.py finished')