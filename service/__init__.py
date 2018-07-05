from flask import Flask
import yaml

from service.database import GHDatabase
from service.utils import jsonify


config_yaml = open('config/test.yml').read()
config = yaml.load(config_yaml)
app = Flask(__name__)
app.config.update(config)
db = GHDatabase(app)
