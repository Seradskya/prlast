from .db_init import db

association_table = db.Table('playlist_to_channel',
     db.Column('playlist', db.Integer, db.ForeignKey('playlist.id'), primary_key=True),
    db.Column('radio_channel', db.Integer, db.ForeignKey('radio_channel.id'), primary_key=True)
)