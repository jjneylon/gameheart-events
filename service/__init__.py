from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

from service.utils import jsonify


config_yaml = open('config/test.yml').read()
config = yaml.load(config_yaml)
app = Flask(__name__)
app.config.update(config)
db = SQLAlchemy(app)
