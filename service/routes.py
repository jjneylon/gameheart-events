from flask import Blueprint

from service.utils import jsonify
from service import config


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/hello')
def hello():
    return "Hello World!"


@api_blueprint.route('/config')
def display_config():
    return jsonify(dict(config), date_fmt='%Y-%m-%dT%H:%M:%S')
