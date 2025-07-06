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
import sys
from flask import Flask
from flask_restful import Resource, Api

import db

# Create a new logging object
log = logging.getLogger(__name__)
log_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)

log.addHandler(log_handler)
log.setLevel(logging.INFO)

log.info('Creating Flask API...')
app = Flask(__name__)
api = Api(app)

class getBookByISBN(Resource):
    def get(self, isbn):
        return db.getBookData(isbn = int(isbn))

class getBookByName(Resource):
    def get(self, name):
        return db.getBookData(name = str(name))

class getBookByID(Resource):
    def get(self, id):
        return db.getBookData(id = int(id))

api.add_resource(getBookByISBN, '/Book/getByISBN')
api.add_resource(getBookByName, '/Book/getByName')
api.add_resource(getBookByID, '/Book/getByID')

if __name__ == '__main__':
    app.run()