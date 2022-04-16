from .db_init import db


class MobileUser(db.Model):
    id = db.Column(db.String, primary_key=True)
    playlists = db.relationship('Playlist', back_populates='user', lazy=True)
