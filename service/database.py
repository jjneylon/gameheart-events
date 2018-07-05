from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column
from flask_sqlalchemy.model import Model


class GHDatabase(SQLAlchemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_registry = {}

    def register_model(self, model_name, model_cls):
        self.model_registry[model_name] = model_cls

    class Column(Column):
        def __init__(self, *args, **kwargs):
            self.methods = kwargs.pop('methods', ['GET', 'PUT', 'PATCH'])
            super().__init__(*args, **kwargs)

    class Model(Model):
        @classmethod
        def get_columns(cls):
            columns = []
            for attr_name in dir(cls):
                attr = getattr(cls, attr_name)
                if isinstance(attr, Column):
                    columns.append((attr_name, attr))
            return columns
