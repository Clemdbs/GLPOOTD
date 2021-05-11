import re

from model.dao.music_dao import MusicDAO
from exceptions import Error, InvalidData


class MusicController:
    """
    Music actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_musics(self):
        with self._database_engine.new_session() as session:
            musics = MusicDAO(session).get_all()
            musics_data = [music.to_dict() for music in musics]
        return musics_data

    def get_music(self, music_id):
        with self._database_engine.new_session() as session:
            music = MusicDAO(session).get(music_id)
            music_data = music.to_dict()
        return music_data

    def create_music(self, data):

        try:
            with self._database_engine.new_session() as session:
                print("a")
                # Save music in database
                music = MusicDAO(session).create(data)
                print("a")
                music_data = music.to_dict()
                return music_data
        except Error as e:
            # log error
            raise e

    def update_music(self, music_id, music_data):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get(music_id)
            music = music_dao.update(music, music_data)
            return music.to_dict()

    def delete_music(self, music_id):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get(music_id)
            music_dao.delete(music)

    def search_music(self, titre, artiste, album):
        # Query database
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get_by_titre_artiste_album(titre, artiste, album)
            if music == None:
                return None
            return music.to_dict()

    def search_music_title(self, titre):
        # Query database
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get_by_titre(titre)
            if music == None:
                return None
            return music.to_dict()