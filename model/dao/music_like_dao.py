from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.music_like import Music_Like
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class Music_LikeDAO(DAO):
    """
    Music_Like Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Music_Like).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_data(self, data):
        try:
            return self._database_session.query(Music_Like).filter_by(id_musique=data['id_musique']).filter_by(id_utilisateur=data['id_utilisateur']).one()
        except NoResultFound:
            return None

    def get_by_user_id(self, user_id):
        try:
            return self._database_session.query(Music_Like).filter_by(id_utilisateur=user_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Music_Like).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            music_like = Music_Like(id_musique=data.get('id_musique'), id_utilisateur=data.get('id_utilisateur'))
            self._database_session.add(music_like)
            self._database_session.flush()
        except IntegrityError:
            raise Error("music_like already exists")
        return music_like

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))