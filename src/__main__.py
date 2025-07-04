# Import modules
import frontend, backend
import logging, logging.handlers
import yaml

# Read the YAML config file
with open('./config/configuration.yaml') as file:
    configuration = yaml.load(file, Loader = yaml.CLoader)

# Create a new logging object
log = logging.getLogger(__name__)

# Create a logging handler based on configuration data
log_handler = logging.handlers.TimedRotatingFileHandler(filename = './logs/library-system', when = configuration['logging']['refresh'], backupCount = configuration['logging']['store'])
log_handler.doRollover()

# Attach that handler to the logger
log.addHandler(log_handler)

# Set verbosity level
log.setLevel(configuration['logging']['level'])

log.debug('LOGGER started')