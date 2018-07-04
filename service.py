from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

from utils import jsonify


config_yaml = open('config/test.yml').read()
app = Flask(__name__)
app.config.update(yaml.load(config_yaml))
db = SQLAlchemy(app)


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/config')
def display_config():
    return jsonify(dict(app.config), date_fmt='%Y-%m-%dT%H:%M:%S')


if __name__ == '__main__':
    app.run()
