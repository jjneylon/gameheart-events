from flask import Blueprint, request

from service import db, config
from service.handlers import (
    handle_put,
)
from service.models import model_registry
from service.utils import jsonify


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/hello')
def hello():
    return "Hello World!"


@api_blueprint.route('/config')
def display_config():
    return jsonify(dict(config), date_fmt='%Y-%m-%dT%H:%M:%S')


@api_blueprint.route('/api/<model_name>', methods=['PUT'])
def put_model(model_name):
    model_cls = model_registry.get(model_name)
    payload = request.json or {}
    status_code, message = handle_put(model_cls, payload, db)
    request.status_code = status_code
    return message
