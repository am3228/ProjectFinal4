from flask import Flask
from flask_assets import Environment


app = Flask(__name__, instance_relative_config=False)

assets = Environment(app)