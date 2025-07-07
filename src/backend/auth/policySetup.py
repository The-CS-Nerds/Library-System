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