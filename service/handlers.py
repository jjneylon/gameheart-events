import json


def handle_get(model_cls, model_id, db):
    response_payload = {}
    model_inst = model_cls.query.get(model_id)
    for column in model_cls.get_columns():
        if 'GET' in column.methods:
            response_payload[column.name] = getattr(model_inst, column.name)

    return 200, json.dumps(response_payload)


def handle_patch(model_cls, model_id, payload, db):
    response_payload = {'id': model_id}
    model_inst = model_cls.query.get(model_id)
    for column in model_cls.get_columns():
        if 'PATCH' in column.methods \
                and column.name in payload.keys() \
                and getattr(model_inst, column.name) != payload[column.name]:
            setattr(model_inst, column.name, payload[column.name])
            response_payload[column.name] = payload[column.name]

    if len(response_payload.keys()) > 1:
        db.session.add(model_inst)
        db.session.commit()

    return 200, json.dumps(response_payload)


def handle_put(model_cls, payload, db):
    model_inst_kwargs = {}
    for column in model_cls.get_columns():
        if 'PUT' in column.methods:
            model_inst_kwargs[column.name] = payload.get(column.name)

    model_inst = model_cls(**model_inst_kwargs)
    db.session.add(model_inst)
    db.session.commit()
    return 201, json.dumps({'model_id': model_inst.id})
