from service.__init__ import db
from sqlalchemy_utils import UUIDType


class Site(db.Model):
    __tablename__ = 'site'
    uuid = db.Column(UUIDType(), primary_key=True, methods=['GET'])
    chapter_uuid = db.Column(UUIDType())
    title = db.Column(db.String(32))
    latitude = db.Column(db.String(32))
    longitude = db.Column(db.String(32))

    events = db.relationship('Event', back_populates='site')


class Event(db.Model):
    __tablename__ = 'event'
    uuid = db.Column(UUIDType(), primary_key=True, methods=['GET'])
    site_uuid = db.Column(UUIDType(), db.ForeignKey('site.uuid'))
    chapter_uuid = db.Column(UUIDType())
    title = db.Column(db.String(32))
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))

    site = db.relationship('Site', back_populates='events')
