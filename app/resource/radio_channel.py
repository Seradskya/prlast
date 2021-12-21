import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import RadioChannel
from app.models.db_init import db
from app.schema.radio_channel import RadioChannelSchema

radio_channel_ns = Namespace('radio_channel', description='Операции для взаимодействия с постами')


@radio_channel_ns.route("/")
class RadioChannelResource(Resource):
    @radio_channel_ns.doc('Get posts')
    @responds(schema=RadioChannelSchema, many=True, api=radio_channel_ns)
    def get(self):
        return RadioChannel.query.all()

    @flask_praetorian.roles_required("admin")
    @radio_channel_ns.doc('Get posts', security='Bearer')
    @accepts(schema=RadioChannelSchema, api=radio_channel_ns)
    def post(self):
        radio_channel = request.parsed_obj
        db.session.add(radio_channel)
        db.session.commit()
        return {'status': 'ok'}
