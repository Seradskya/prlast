import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import MobileUser
from app.models.db_init import db
from app.schema.mobile_user import MobileUserSchema
from app.resource.init_guard import guard

mobile_user_ns = Namespace('mobile_user', description='Операции для взаимодействия с юзерами')


@mobile_user_ns.route("/")
class MobileUserResource(Resource):
    @mobile_user_ns.doc('User Playlist', security='Bearer')
    @accepts(schema=MobileUserSchema, api=mobile_user_ns)
    def post(self):
        user = request.parsed_obj
        mobile_user = MobileUser(id=user.id)
        db.session.add(mobile_user)
        db.session.commit()
        return {'status': 'ok'}
