import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.models import RadioChannel
from app.models import Playlist
from app.models.db_init import db
from app.schema.playlist import PlaylistSchema, PlaylistAddChannelSchema
from app.resource.init_guard import guard

playlist_ns = Namespace('playlist', description='Операции для взаимодействия с плейлистами')


@playlist_ns.route("/add/<string:user_id>")
class PlaylistResource(Resource):
    @playlist_ns.doc('Add Playlist', security='Bearer')
    @accepts(schema=None, api=playlist_ns)
    def post(self, user_id):
        playlist = Playlist()
        playlist.user_id = user_id
        db.session.add(playlist)
        db.session.commit()
        return {'id': playlist.id}


@playlist_ns.route("/add_channel")
class PlaylistAddChannelResource(Resource):
    @playlist_ns.doc('add channel to Playlist', security='Bearer')
    @accepts(schema=PlaylistAddChannelSchema, api=playlist_ns)
    def post(self):
        data = request.parsed_obj
        playlist = db.session.query(Playlist).filter_by(id=data.playlist_id).first()
        channel = db.session.query(RadioChannel).filter_by(id=data.channel_id).first()
        playlist.channels.append(channel)
        db.session.commit()
        return {'status': 'ok'}


@playlist_ns.route("/del_channel")
class PlaylistDellChannelResource(Resource):
    @playlist_ns.doc('delete channel from Playlist', security='Bearer')
    @accepts(schema=PlaylistAddChannelSchema, api=playlist_ns)
    def post(self):
        data = request.parsed_obj
        playlist = db.session.query(Playlist).filter_by(id=data.playlist_id).first()
        channel = db.session.query(RadioChannel).filter_by(id=data.channel_id).first()
        playlist.channels.remove(channel)
        db.session.commit()
        return {'status': 'ok'}


@playlist_ns.route("/<int:playlist_id>")
class PlaylistChangeResource(Resource):
    @flask_praetorian.auth_required
    @playlist_ns.doc('Get playlist channels', security='Bearer')
    def get(self, playlist_id):
        playlist = db.session.query(Playlist).filter_by(id=playlist_id).first()
        result = {}
        for channel in playlist.channels:
            channel: RadioChannel
            result[channel.id] = {"name": channel.name,
                                  "radio_stream_url": channel.radio_stream_url,
                                  "radio_cover_url": channel.cover_url,
                                  "is_active": channel.is_active,
                                  "is_popular": channel.is_popular}
        return result

    @flask_praetorian.auth_required
    @playlist_ns.doc('Playlist editing', security='Bearer')
    @accepts(schema=PlaylistSchema, api=playlist_ns)
    @responds(schema=PlaylistSchema, api=playlist_ns, status_code=200)
    def put(self, playlist_id):
        data = request.parsed_obj
        db.session.query(Playlist).filter_by(id=playlist_id).update(
            {'user_id': data.user_id}
        )
        db.session.commit()
        return db.session.query(Playlist).get(playlist_id)

    @flask_praetorian.auth_required
    @playlist_ns.doc('Playlist editing delete', security='Bearer')
    @responds(schema=None, api=playlist_ns, status_code=200)
    def delete(self, playlist_id):
        db.session.query(Playlist).filter_by(id=playlist_id).delete(synchronize_session=False)
        db.session.commit()
        return 'Удалено'

