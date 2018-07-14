from flask import Blueprint, request

from service import db
from service.handlers import (
    handle_get,
    handle_patch,
    handle_put,
)
from service.models import model_registry


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/api/<model_name>/<model_id>', methods=['GET'])
def get_model(model_name, model_id):
    model_cls = model_registry.get(model_name)
    status_code, message = handle_get(model_cls, model_id, db)
    request.status_code = status_code
    return message


@api_blueprint.route('/api/<model_name>/<model_id>', methods=['PATCH'])
def patch_model(model_name, model_id):
    model_cls = model_registry.get(model_name)
    payload = request.json or {}
    status_code, message = handle_patch(model_cls, model_id, payload, db)
    request.status_code = status_code
    return message


@api_blueprint.route('/api/<model_name>', methods=['POST'])
def post_new_model(model_name):
    model_cls = model_registry.get(model_name)
    payload = request.form.to_dict() if request.form else {}
    status_code, message = handle_put(model_cls, payload, db)
    request.status_code = status_code
    return message


@api_blueprint.route('/api/<model_name>/model_id', methods=['POST'])
def post_update_model(model_name, model_id):
    model_cls = model_registry.get(model_name)
    payload = request.form.to_dict() if request.form else {}
    status_code, message = handle_patch(model_cls, model_id, payload, db)
    request.status_code = status_code
    return message


@api_blueprint.route('/api/<model_name>', methods=['PUT'])
def put_model(model_name):
    model_cls = model_registry.get(model_name)
    payload = request.json or {}
    status_code, message = handle_put(model_cls, payload, db)
    request.status_code = status_code
    return message
