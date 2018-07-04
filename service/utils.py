import datetime
import json


def json_format(target, date_fmt):
    if isinstance(target, dict):
        return {key: json_format(obj, date_fmt) for key, obj in target.items()}
    elif isinstance(target, list):
        return [json_format(i, date_fmt) for i in target]
    elif isinstance(target, datetime.datetime):
        return datetime.datetime.strftime(target, date_fmt)
    elif isinstance(target, datetime.timedelta):
        return str(target)
    else:
        return target


def jsonify(target, date_fmt='%Y-%m-%dT%H:%M:%S'):
    return json.dumps(json_format(target, date_fmt))
