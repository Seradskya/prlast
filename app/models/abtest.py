from .db_init import db


class Abtest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(1000))
    scen_id = db.Column(db.Integer)
    flag = db.Column(db.Integer)

