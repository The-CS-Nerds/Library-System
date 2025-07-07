#    This program is for the hosting of a webpage, through which authentication (via Casdoor) and API requests to the backend (via Casbin) will occur.
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
# Import modules
from flask import Flask
import logging, sys
import requests

# Create a new logging object
log = logging.getLogger(__name__)
log_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)

log.addHandler(log_handler)
log.setLevel(20)

if __name__ == "__main__":
    log.info('Creating Flask app...')

    # Create a flask app
    app = Flask(__name__)
    log.info('Created Flask app.')

    log.info('Creating page decorators...')
    # Create a home page
    @app.route("/")
    def index():
        return "<p>Under Construction</p>"

    log.info('Created page decorators.')
    log.info('Frontend exited.')