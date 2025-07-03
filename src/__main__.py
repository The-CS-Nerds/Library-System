from yaml import safe_load as load_yaml
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Under Construction</p>"