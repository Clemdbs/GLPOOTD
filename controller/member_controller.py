import re

from model.dao.member_dao import MemberDAO
from exceptions import Error, InvalidData


class MemberController:
    """
    Member actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_members(self):
        with self._database_engine.new_session() as session:
            members = MemberDAO(session).get_all()
            members_data = [member.to_dict() for member in members]
        return members_data

    def get_member(self, member_id):
        with self._database_engine.new_session() as session:
            member = MemberDAO(session).get(member_id)
            member_data = member.to_dict()
        return member_data

    def create_member(self, data):
        self.check_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                member = MemberDAO(session).create(data)
                member_data = member.to_dict()
                return member_data
        except Error as e:
            # log error
            raise e

    def update_member(self, member_id, member_data):
        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get(member_id)
            member = member_dao.update(member, member_data)
            return member.to_dict()

    def delete_member(self, member_id):
        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get(member_id)
            member_dao.delete(member)

    def search_member(self, email):
        # Query database
        with self._database_engine.new_session() as session:
            member_dao = MemberDAO(session)
            member = member_dao.get_by_email(email)
            return member.to_dict()

    def check_data(self, data):
        email = data['email']
        pseudo = data['pseudo']
        mot_de_passe = data['mot_de_passe']
        sexe = data['sexe']
        pays = data['pays']
        print(data, "data")

        #Test du remplissage :
        if email == "" or pseudo == "" or sexe == "Sexe" or pays == "Pays":
            return 'Veuillez remplir tous les champs'

        #Test du mail :
        if "@" not in email:
            return 'Votre adresse mail n\'est pas valide'
        indice = email.index('@')
        analyse = email[indice:]
        if "." not in analyse:
            return 'Votre adresse mail n\'est pas valide'

        #Test du mot de passe :
        # On ne veut pas d'espace dans le mot de passe
        if " " in mot_de_passe:
            return 'Votre mot de passe ne peut pas avoir d\'espace... !'
        # Tout d'abord, si le mot de passe à une longueur inférieure à 6 (pour une sécurité)
        if len(mot_de_passe) < 6:
            return 'Votre mot de passe doit au minimum contenir 6 caractères !'
        print("test")
        return True

    def connection(self, email, mot_de_passe):
        member = self.search_member(email)
        if(member['mot_de_passe'] == mot_de_passe):
            return True
        return False