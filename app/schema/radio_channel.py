from marshmallow_sqlalchemy import auto_field

from app.models import RadioChannel
from .init_ma import ma


class RadioChannelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RadioChannel
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)

