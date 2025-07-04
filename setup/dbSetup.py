import yaml
import mysql.connector
import logging
import subprocess as sp

log = logging.getLogger(__name__)

log.info("dbSetup.py started")

def loadEnv():
    try:
        with open('../config/configuration.yaml', 'r') as file:
            config = yaml.safe_load(file)
            hostname = config['database']['hostname']
            log.debug('Hostname loaded from config')
            port = config['database']['port']
            log.debug('Port loaded from config')
            username = config['database']['username']
            log.debug('Username loaded from config')
            password = config['database']['password']
            log.debug('Password loaded from config')
            return hostname, port, username, password
    except Exception as e:
        log.error(f"Error loading configuration: {e}")
        return None

def generateSetupSQL(config):
    try:
        setup_sql_path = "../config/setup.sql"
        with open(setup_sql_path, "w") as file:
            file.write(f"CREATE DATABASE IF NOT EXISTS {config['database_name']};\n")
            file.write(f"CREATE USER '{config['username']}'@'localhost' IDENTIFIED BY '{config['password']}';\n")
            file.write(f"GRANT ALL PRIVILEGES ON {config['database_name']}.* TO '{config['username']}'@'localhost';\n")
            file.write("FLUSH PRIVILEGES;\n")
        log.info("setup.sql file generated successfully.")
        return setup_sql_path
    except Exception as e:
        log.error(f"Error generating setup.sql file: {e}")
        return None

def newMySQLinstance():
    generateSetupSQL(loadEnv())
    sp.run(
            ['sudo', 'mysql', '-u', 'root', '-p' + password, '<', sql_file_path],
            check=True
        )


def doesDbExist(dbName):
    if loadEnv():
        hostname, port, username, password = loadEnv()
        database = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
        )
        cursor = database.cursor()
        tableList = cursor.fetchall()
        if dbName in tableList:
            log.info(f"Database {dbName} exists")
            return True
        else:
            log.info(f"Database {dbName} does not exist")
            return False
    else:
        newMySQLinstance()
        return doesDbExist(dbName)