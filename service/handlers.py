import json


def handle_put(model_cls, payload, db):
    model_inst_kwargs = {}
    for column in model_cls.get_columns():
        if 'PUT' in column.methods:
            model_inst_kwargs[column.name] = payload.get(column.name)

    model_inst = model_cls(**model_inst_kwargs)
    db.session.add(model_inst)
    db.session.commit()
    return 201, json.dumps({'model_created': model_inst.id})


def handle_get(model_cls, model_id, db):
    response_payload = {}
    model_inst = model_cls.query.get(model_id)
    for column in model_cls.get_columns():
        if 'GET' in column.methods:
            response_payload[column.name] = getattr(model_inst, column.name)

    return 200, json.dumps(response_payload)
