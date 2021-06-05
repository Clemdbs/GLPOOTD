from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.member import Member
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class MemberDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Member).filter_by(id=id).order_by(Member.email).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Member).order_by(Member.email).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_email(self, email: str):
        try:
            return self._database_session.query(Member).filter_by(email=email)\
                .order_by(Member.email).one()
        except NoResultFound:
            return None

    def create(self, data: dict):
        try:
            member = Member(email=data.get('email'), pseudo=data.get('pseudo'), mot_de_passe=data.get('mot_de_passe'), genre=data.get('genre'))
            self._database_session.add(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return member

    #C'est à faire !
    def update(self, member: Member, data: dict):
        if 'email' in data:
            member.email = data['email']
        if 'pseudo' in data:
            member.pseudo = data['pseudo']
        if 'mot_de_passe' in data:
            member.mot_de_passe = data['mot_de_passe']
        if 'genre' in data:
            member.genre = data['genre']
        try:
            self._database_session.merge(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return member

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
