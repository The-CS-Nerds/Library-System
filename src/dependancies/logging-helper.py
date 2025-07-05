import logging, logging.handlers
import yaml, sys

def createLogs():
# Read the YAML config file
    with open('../config/docker-compose.yaml') as file:
        compose = yaml.safe_load(file)

    # Create a new logging object
    log = logging.getLogger(__name__)

    if compose['x-logging']['logToFile'] == 1: # if logging to file is enabled, write to file
        logDir = './logs'
        logDir.mkdir(parents=True, exist_ok=True)
        logFile = logDir / "library-system.log"
        # Create a logging handler based on configuration data
        file_log_handler = logging.handlers.TimedRotatingFileHandler(filename = logFile, when = compose['x-logging']['refresh'], backupCount = compose['x-logging']['store'])
        file_log_handler.doRollover()
        # Attach that handler to the logger
        log.addHandler(file_log_handler)

    console_log_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(console_log_handler)

    # Set verbosity level
    log.setLevel(compose['x-logging']['level'])

    log.info('LOGGER started')