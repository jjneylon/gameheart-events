import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

from service.utils import jsonify


service_mode = os.environ.get('SERVICE_MODE', 'local')
config_yaml = open('config/{}.yml'.format(service_mode)).read()
config = yaml.load(config_yaml)
app = Flask(__name__)
app.config.update(config)
db = SQLAlchemy(app)
