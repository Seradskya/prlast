import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import RadioChannel
from app.models.db_init import db
from app.schema.radio_channel import RadioChannelSchema
from app.resource.init_guard import guard

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


@radio_channel_ns.route("/<int:radio_id>")
class RadioChannelChangeResource(Resource):
    @flask_praetorian.auth_required
    @radio_channel_ns.doc('Radio data', security='Bearer')
    @responds(schema=RadioChannelSchema, api=radio_channel_ns, status_code=200)
    def get(self, radio_id):
        return db.session.query(RadioChannel).get(radio_id)

    """@flask_praetorian.auth_required
    @radio_channel_ns.doc('Radio editing', security='Bearer')
    @accepts(schema=RadioChannelSchema, api=radio_channel_ns)
    @responds(schema=RadioChannelSchema, api=radio_channel_ns, status_code=200)
    def put(self, radio_id):
        radio = request.parsed_obj
        if radio.id is not None:
            radio.id = guard.extract_jwt_token(guard.read_token())['id']
        if radio_id.id != guard.extract_jwt_token(guard.read_token())['id']:
            return {'status': 'error', 'message': 'Permission denied'}, 403
        db.session.add(radio)
        db.session.commit()
        return radio"""

    @radio_channel_ns.doc('User editing', security='Bearer')
    @accepts(schema=RadioChannelSchema, api=radio_channel_ns)
    @responds(schema=RadioChannelSchema, api=radio_channel_ns, status_code=200)
    def put(self, radio_id):
        radio = request.parsed_obj
        if radio.id is not None:
            radio.id = guard.extract_jwt_token(guard.read_token())['id']
        if radio_id.id != guard.extract_jwt_token(guard.read_token())['id']:
            return {'status': 'error', 'message': 'Permission denied'}, 403
        db.session.add(radio)
        db.session.commit()
        return radio