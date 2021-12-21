from app.models import RadioChannel
from .init_ma import ma


class RadioChannelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RadioChannel
        load_instance = True
        include_fk = True
