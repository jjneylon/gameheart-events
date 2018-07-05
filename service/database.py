from flask_sqlalchemy.model import *
from sqlalchemy.orm import *
from sqlalchemy.schema import *
from sqlalchemy.sql.base import *
from sqlalchemy.types import *
from sqlalchemy_utils import UUIDType


class GHColumn(Column):
    def __init__(self, *args, **kwargs):
        self.methods = kwargs.pop('methods', ['GET', 'PUT', 'PATCH'])
        super().__init__(*args, **kwargs)


class GHModel(Model):
    @classmethod
    def get_columns(cls):
        columns = []
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if isinstance(attr, Column):
                columns.append((attr_name, attr))
        return columns
