# Import modules
from flask import Flask
import logging, sys

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