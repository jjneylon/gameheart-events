import json


def handle_put(model_cls, payload, db):
    model_inst_kwargs = {}
    for column_name, column in model_cls.get_columns():
        if 'PUT' in column.methods:
            model_inst_kwargs[column_name] = payload.get(column_name)

    model_inst = model_cls(**model_inst_kwargs)
    db.session.add(model_inst)
    db.session.commit()
    return 201, json.dumps({'model_created': model_inst.uuid})
