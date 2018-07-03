from service import db
from sqlalchemy_utils import UUIDType


class Event(db.Model):
    uuid = db.Column(UUIDType(), primary_key=True)
    site_uuid = db.Column(UUIDType())
    chapter_uuid = db.Column(UUIDType())
    title = db.Column(db.String(32))
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
