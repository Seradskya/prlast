from marshmallow_sqlalchemy import auto_field

from app.models import Abtest
from .init_ma import ma


class AbtestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Abtest
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)

