#    This program is for communicating with a PostgreSQL database using Casbin authentication.
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
import logging
import psycopg
import os
import uuid
from email_validator import validate_email, EmailNotValidError
from casbin import Enforcer

from casbin import Enforcer

log = logging.getLogger(__name__)

log.info('Reading DB password...')

db_pass = os.environ['DB_PASS']

log.info('Read DB password')

class APIException(Exception):
    pass

def sendSQLCommand(command, userID, table, verified = True, fetch = 1): # NO USER INPUT SHOULD BE SENT DIRECTLY HERE
    verb = command.strip().split()[0].upper()
    action_map = {
        "SELECT": "read",
        "INSERT": "write",
        "UPDATE": "write",
        "DELETE": "delete", #@HippoProgrammer Please update this as I know not much SQL
    }
    action = action_map.get(verb)
    if Enforcer.enforce(userID, table, "*", action, verified):
        log.debug("User is authorized to perform this action")
        log.info('Connecting to postgres DB...')
        with psycopg.connect(f"postgres://library:{db_pass}@db:5432/library") as conn: # create a connection to the db
            db_pass.delete()
            try:
                log.info('Connected to postgres DB.')
                log.info('Opening cursor...')
                with conn.cursor() as cur: # open a cursor
                    log.info('Opened cursor.')
                    cur.execute(command)
                    log.info('Sent command.')

                    if fetch == 1:
                        return cur.fetchone()
                    elif fetch > 1:
                       return cur.fetchmany(fetch)
                    elif fetch == 0:
                        return None
                    elif fetch == -1:
                        return cur.fetchall()
                    else:
                        raise APIException('Invalid fetch value provided to sendSQLCommand.')
            except Exception as e:
                conn.rollback()
                log.error(e)
            else:
                conn.commit()
                log.info('Committed.')
            finally:
                conn.close()
                log.info('Connection closed.')
    else:
        log.error("User is not authorized to perform this action")

def getBookData(id:int = 0, isbn:int = 0, title:str = '', author:str = '', published:str = '', description:str = ''):
    args = {'id':id, 'isbn':isbn, 'title':title, 'author':author, 'published':published, 'description':description}
    provided = [arg for arg in list(args.items()) if arg[1]] # filters out provided values
    if len(provided) == 1: # if only one
        data = sendSQLCommand(command = f'SELECT {provided[0][0]} FROM books WHERE isbn = {provided[0][1]}', fetch = 1) # SELECT column FROM books WHERE isbn = value
        return data
    elif len(provided) == 0: # if none provided
        raise APIException('You must provide one argument to getBookData.')
    else:
        raise APIException('You must only provide one argument to getBookData.')

class user:
    def __init__(self, userID: int, email: str, role: str = 'student'):
        try:
            valid = validate_email(email)
            self.email = valid.email
        except EmailNotValidError as e:
            log.error(f"Invalid email address: {email}")
        self.userID = userID
        self.id = str(uuid.uuid4())
        self.role = role
    def SQLStore(self):
        try:
            sendSQLCommand(
                command="INSERT INTO users (id, user_id, email) VALUES (%s, %s, %s)",
                params=(self.id, self.userID, self.email),
                userID='admin', # Needs to updated later on
                table='users',
                verified=True,
                fetch=0
            )
        except Exception as e:
            log.error(f"Failed to store user {self.userID} in database: {e}")
    def addToCasbin(self):
        try:
            enforcer = Enforcer("model.conf", "policy.csv")
            enforcer.add_policy("user", self.id, "read", "book")
            enforcer.add_grouping_policy(self.id, "group", self.role)
            enforcer.save_policy()
        except Exception as e:
            log.error(f"Failed to add user {self.userID} to Casbin: {e}")
        else:
            log.info(f"User {self.userID} added to Casbin successfully.")