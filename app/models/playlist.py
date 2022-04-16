from .association_table import association_table
from .db_init import db


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('mobile_user.id'))
    user = db.relationship("MobileUser", back_populates='playlists', lazy=True)
    channels = db.relationship('RadioChannel', secondary=association_table, lazy=True)
