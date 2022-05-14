from marshmallow_sqlalchemy import auto_field

from app.models import Percent
from .init_ma import ma


class PercentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Percent
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)

