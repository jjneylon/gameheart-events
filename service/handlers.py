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
