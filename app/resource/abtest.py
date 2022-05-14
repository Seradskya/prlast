import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import RadioChannel
from app.models import Abtest
from app.models.db_init import db
from app.schema.abtest import AbtestSchema
from app.resource.init_guard import guard
import random

abtest_ns = Namespace('abtest', description='Операwции для проведения  тестов')


@abtest_ns.route("/add/<string:user_id>/<int:scen_id>/<int:flag>")
class AbtestResource(Resource):
    @abtest_ns.doc('Add record', security='Bearer')
    @accepts(schema=None, api=abtest_ns)
    def post(self, user_id, scen_id, flag):
        abtest = Abtest()
        abtest.user_id = user_id
        abtest.scen_id = scen_id
        abtest.flag = flag

        db.session.add(abtest)
        db.session.commit()
        return {'status': 'ok'}


@abtest_ns.route("get_lucky/<int:scen_id>")
class AbtestLuckyResource(Resource):
    @abtest_ns.doc('Get lucky results', security='Bearer')
    def get(self, scen_id):
        results = db.session.query(Abtest).filter_by(Abtest.scen_id == scen_id & Abtest.flag == 0).all()
        result = 0
        for test in results:
            result = result + 1
        return result


@abtest_ns.route("get_all/<int:scen_id>")
class AbtestLuckyResource(Resource):
    @abtest_ns.doc('Get all results', security='Bearer')
    def get(self, scen_id):
        results = db.session.query(Abtest).filter_by(Abtest.scen_id == scen_id & Abtest.flag == 1).all()
        result = 0
        for test in results:
            result = result + test.flag
        return result


@abtest_ns.route("get_convers/<int:scen_id>")
class AbtestLuckyResource(Resource):
    @abtest_ns.doc('Get convers', security='Bearer')
    def get(self, scen_id):
        results_lucky = db.session.query(Abtest).filter_by(Abtest.scen_id == scen_id & Abtest.flag == 0).all()
        result_lucky = 0
        for test in results_lucky:
            result_lucky = result_lucky + 1
        results_all = db.session.query(Abtest).filter_by(Abtest.scen_id == scen_id & Abtest.flag == 1).all()
        result_all = 0
        for test in results_all:
            result_all = result_all + test.flag
        result = result_lucky/result_all
        return result



