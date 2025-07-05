# Import modules
import yaml
import logging
from secrets import token_urlsafe as rand_token
import os
import subprocess
import time

# Create a new logging object
log = logging.getLogger(__name__)

with open('/run/secrets/db_pass') as file:
    db_pass = file.read()