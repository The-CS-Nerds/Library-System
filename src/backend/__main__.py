# Import modules
import yaml
import logging
import time
import psycopg

# Create a new logging object
log = logging.getLogger(__name__)

with open('/run/secrets/db_pass') as file:
    db_pass = file.read()

with psycopg.connect(f"postgres://library:{password}@db:5432/library") as conn: # create a connection to the db
    with conn.cursor() as cur: # open a cursor
        pass # ADD SQL COMMANDS HERE
        conn.commit()