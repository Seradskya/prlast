from .db_init import db


class Percent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scen_id = db.Column(db.Integer)
    probability = db.Column(db.Integer)


