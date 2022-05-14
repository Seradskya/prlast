import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import Percent
from app.models.db_init import db
from app.schema.percent import PercentSchema
from app.resource.init_guard import guard
import random

percent_ns = Namespace('percent', description='Операwции для получения сценария по вероятности')


@percent_ns.route("/add/<int:scen_id>/<int:probability>/")
class PercentResource(Resource):
    @percent_ns.doc('Add record', security='Bearer')
    @accepts(schema=None, api=percent_ns)
    def post(self, scen_id,  probability):
        record = Percent()
        record.scen_id = scen_id
        record.probability = probability

        db.session.add(record)
        db.session.commit()
        return {'status': 'ok'}


@percent_ns.route("/<int:scen_id>")
class PercentChangeResource(Resource):
    @flask_praetorian.auth_required
    @percent_ns.doc('Percent data', security='Bearer')
    @responds(schema=PercentSchema, api=percent_ns, status_code=200)
    def get(self, scen_id):
        return db.session.query(Percent).get(scen_id)

    @flask_praetorian.auth_required
    @percent_ns.doc('Percent editing', security='Bearer')
    @accepts(schema=PercentSchema, api=percent_ns)
    @responds(schema=PercentSchema, api=percent_ns, status_code=200)
    def put(self, scen_id):
        data = request.parsed_obj
        scen_id = data.scen_id
        probability = data.probability
        db.session.query(Percent).filter_by(scen_id=scen_id).update(
            {'probability': probability}
        )
        db.session.commit()
        return db.session.query(Percent).get(scen_id)


@percent_ns.route("/get_random/")
class PercentRandomResource(Resource):
    @percent_ns.doc('Get random record', security='Bearer')
    @accepts(schema=None, api=percent_ns)
    def get(self):
        probability_first = db.session.query(Percent).filter_by(Percent.scen_id == 1).first()
        probability_second = db.session.query(Percent).filter_by(Percent.scen_id == 2).first()
        result = random.choices([1, 2], weights=[probability_first.probability/100, probability_second.probability/100])[0]

        return {'scen_id': result}



