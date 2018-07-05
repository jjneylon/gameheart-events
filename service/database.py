from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import Column


class GHDatabase(SQLAlchemy):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Column(Column):
        def __init__(self, *args, **kwargs):
            self.methods = kwargs.pop('methods', ['GET', 'PUT', 'PATCH'])
            super().__init__(*args, **kwargs)
