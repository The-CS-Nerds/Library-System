# Import modules
from flask import Flask
import logging

# Create a new logging object
log = logging.getLogger(__name__)

# Create a flask app
app = Flask(__name__)

# Create a home page
@app.route("/")
def index():
    return "<p>Under Construction</p>"
