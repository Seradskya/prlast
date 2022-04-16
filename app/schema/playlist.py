import marshmallow_dataclass
from marshmallow_sqlalchemy import auto_field

from app.models import Playlist
from .init_ma import ma


class PlaylistAddChannelData:
    channel_id: int
    playlist_id: int


PlaylistAddChannelSchema = marshmallow_dataclass.class_schema(PlaylistAddChannelData)


class PlaylistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Playlist
        load_instance = True
        include_fk = True

    id = auto_field(dump_only=True)