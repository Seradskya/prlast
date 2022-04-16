from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api

from . import resource
from .config import Config
from .models.db_init import db
from .resource.init_guard import guard
from .schema.init_ma import ma

cors = CORS()
migrate = Migrate()
api = Api(authorizations={
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    },
})

from .models import *


def create_app():
    config = Config  # Todo: fixme!!!

    app = Flask(__name__)
    app.config.from_object(config)
    app.debug = True
    from app.models import User
    with app.app_context():
        guard.init_app(app, User)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    api.init_app(app)
    api.add_namespace(resource.user_ns)
    api.add_namespace(resource.radio_channel_ns)
    api.add_namespace(resource.mobile_user_ns)
    api.add_namespace(resource.playlist_ns)

    cors.init_app(app)

    return app