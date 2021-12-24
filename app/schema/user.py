from marshmallow_sqlalchemy import auto_field

from app.models import User
from .init_ma import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True

    hashed_password = auto_field(load_only=True)