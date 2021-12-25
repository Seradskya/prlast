from .db_init import db


class RadioChannel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cover_url = db.Column(db.String(1000))
    radio_stream_url = db.Column(db.String(1000))
    is_active = db.Column(db.Boolean, default=True)
    is_popular = db.Column(db.Boolean, default=True)

    @property
    def identity(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has an ``identity`` instance
        attribute or property that provides the unique id of the user instance
        """
        return self.id

    @classmethod
    def identify(cls, radio_id):
        """
        *Required Method*
        flask-praetorian requires that the user class implements an ``identify()``
        class method that takes a single ``id`` argument and returns user instance if
        there is one that matches or ``None`` if there is not.
        """
        return db.session.query(cls).get(radio_id)