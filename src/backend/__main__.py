# Import modules
import yaml
import logging
import time
import psycopg
import sys

# Create a new logging object
log = logging.getLogger(__name__)
log_handler = logging.StreamHandler(sys.stdout)

log.addHandler(log_handler)
log.setLevel(logging.INFO)

log.info('Reading DB password...')

with open('/run/secrets/db_pass') as file:
    db_pass = file.read()

log.info('Read DB password.')

log.info('Connecting to postgres DB...')
with psycopg.connect(f"postgres://library:{db_pass}@db:5432/library") as conn: # create a connection to the db
    log.info('Connected to postgres DB.')
    log.info('Opening cursor...')
    with conn.cursor() as cur: # open a cursor
        log.info('Opened cursor.')
        pass # ADD SQL COMMANDS HERE
        conn.commit()

log.info('Backend exited.')