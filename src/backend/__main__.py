# Import modules
import yaml
import logging
from secrets import token_urlsafe as rand_token
import os
import subprocess
import time

# Create a new logging object
log = logging.getLogger(__name__)

cwd = os.getcwd()

host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
database = '*'
username = '*'


# Write a pgpass file
with open(f'{cwd}/.pgpass','w') as file:
    file.write(f'{host}:{port}:{database}:{username}:{rand_token(512)}')
subprocess.run(f'chmod 0600 {cwd}/.pgpass')
os.environ['PGPASSFILE'] = f'{cwd}/.pgpass'

while True:
    try:
        subprocess.run('pg_isready -U library')
        break
    except subprocess.CalledProcessError:
        time.sleep(5)