from .db_init import db


class RadioChannel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cover_url = db.Column(db.String(1000))
    radio_stream_url = db.Column(db.String(1000))
    is_active = db.Column(db.String(1000))
    is_popular = db.Column(db.String(1000))
