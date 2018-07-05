from flask import request
import json

from service.models import (
    Event,
    Site,
)


def handle_put():
    try:
        payload = json.loads(request.data)
    except TypeError:
        return 400, '{"error"; "Request payload not json serializable"}'

    
