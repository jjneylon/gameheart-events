from sqlalchemy.inspection import inspect
from service import db


class APIColumn(db.Column):
    def __init__(self, *args, **kwargs):
        self.methods = kwargs.pop('methods', ['GET', 'PATCH', 'POST', 'PUT']) or []
        super().__init__(*args, **kwargs)


def get_columns(cls):
    return [col for col in inspect(cls).columns]


db.APIColumn = APIColumn
setattr(db.Model, 'get_columns', classmethod(get_columns))
