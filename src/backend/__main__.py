#    This repository is made for the purpose of managing online library systems
#    Copyright (C) <2025>  <The CS Nerds>
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