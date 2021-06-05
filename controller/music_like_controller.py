import re

from model.dao.music_like_dao import Music_LikeDAO
from exceptions import Error, InvalidData


class Music_LikeController:
    """
    Music Like actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_musics_like(self):
        with self._database_engine.new_session() as session:
            musics_like = Music_LikeDAO(session).get_all()
            musics_data = [music.to_dict() for music in musics_like]
        return musics_data

    def create_music_like(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save music in database
                music_like = Music_LikeDAO(session).create(data)
                music_data = music_like.to_dict()
                return music_data
        except Error as e:
            # log error
            raise e

    def delete_music(self, music_id):
        with self._database_engine.new_session() as session:
            music_dao = Music_LikeDAO(session)
            music_like = music_dao.get(music_id)
            music_dao.delete(music_like)

    def get_id_musiques_like_by_user(self, user_id):
        with self._database_engine.new_session() as session:
            music_like = Music_LikeDAO(session).get_by_user_id(user_id)
            music_data = music_like
            for i in range(len(music_data)):
                music_data[i] = music_data[i].to_dict()
        return music_data

    def get_id_by_data(self, data):
        with self._database_engine.new_session() as session:
            music_like = Music_LikeDAO(session).get_by_data(data)
            if music_like == None:
                return None
            music_data = music_like.to_dict()
        return music_data

    def reinitialisation_de_la_base_de_donnees(self):
        musiques = self.list_musics_like()
        tableau_des_id = []
        for musique in musiques:
            id = musique['id']
            tableau_des_id.append(id)
        for id in tableau_des_id:
            self.delete_music(id)