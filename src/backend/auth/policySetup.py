from pathlib import Path
import os
import sys

from casbin import Enforcer, persist
from casbin_sqlalchemy_adapter import Adapter
from sqlalchemy import create_engine

MODEL_PATH   = Path(__file__).parent / "model.conf"
POLICY_PATH = Path(__file__).parent / "policy.csv"

'''
WE NEED TO SORT OUT:
DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

They need to be done securly.

#26 - Security
'''


DSN = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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