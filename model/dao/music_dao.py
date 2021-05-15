from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc

from model.mapping.music import Music
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class MusicDAO(DAO):
    """
    Music Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Music).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Music).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_titre_artiste_album(self, titre: str, artiste: str, album: str):
        try:
            return self._database_session.query(Music).filter_by(album=album).filter_by(artiste=artiste).filter_by(titre=titre)\
                .order_by(Music.titre).one()
        except NoResultFound:
            return None

    def get_by_titre(self, titre: str):
        try:
            return self._database_session.query(Music).filter_by(titre=titre)\
                .order_by(Music.titre).one()
        except NoResultFound:
            return None

    def create(self, data: dict):
        try:
            music = Music(titre=data.get('titre'), artiste=data.get('artiste'), album=data.get('album'), type=data.get('type'), chemin_musique=data.get('chemin_musique'), chemin_cover_image=data.get('chemin_cover_image'),stream=0)
            self._database_session.add(music)
            self._database_session.flush()
        except IntegrityError:
            raise Error("music already exists")
        return music

    def update(self, music: Music, data: dict):
        if 'titre' in data:
            music.titre = data['titre']
        if 'artiste' in data:
            music.artiste = data['artiste']
        if 'album' in data:
            music.album = data['album']
        if 'type' in data:
            music.type = data['type']
        if 'chemin_musique' in data:
            music.chemin_musique = data['chemin_musique']
        if 'chemin_cover_image' in data:
            music.chemin_cover_image = data['chemin_cover_image']
        if 'stream' in data:
            music.stream = data['stream']
        try:
            self._database_session.merge(music)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return music

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))

    def ajout_stream(self, music: Music):
        music.stream += 1
        try:
            self._database_session.merge(music)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur stream")

    def get_top(self):
        try:
            #On limite à 5 pour avoir les 5 musiques les plus écoutées (triées par ordre décroissant du nombre d'écoute)
            return self._database_session.query(Music).order_by(desc(Music.stream)).limit(3).all()
        except NoResultFound:
            return None
