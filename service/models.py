from service.database import db


class Site(db.Model):
    __tablename__ = 'site'
    id = db.APIColumn(db.Integer, primary_key=True, methods=['GET'])
    chapter_id = db.APIColumn(db.Integer)
    title = db.APIColumn(db.String(32))
    latitude = db.APIColumn(db.String(32))
    longitude = db.APIColumn(db.String(32))

    events = db.relationship('Event', back_populates='site')


class Event(db.Model):
    __tablename__ = 'event'
    id = db.APIColumn(db.Integer, primary_key=True, methods=['GET'])
    site_id = db.APIColumn(db.Integer, db.ForeignKey('site.id'))
    chapter_id = db.APIColumn(db.Integer)
    title = db.APIColumn(db.String(32))
    start_time = db.APIColumn(db.DateTime(timezone=True))
    end_time = db.APIColumn(db.DateTime(timezone=True))

    site = db.relationship('Site', back_populates='events')


model_registry = {
    'site': Site,
    'event': Event
}
