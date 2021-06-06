from vue.common import Common


class MemberVue:
    """
    Member Vue
    Members interface features
    """

    def __init__(self, member_controller):
        self._member_controller = member_controller
        self._common = Common()

    def add_member(self, informations):
        # Show subscription formular
        data = {}
        print("Spotify user information")
        print(informations)
        print()
        data['email'] = informations[0]
        data['pseudo'] = informations[1]
        data['mot_de_passe'] = informations[2]
        data['genre'] = informations[3]
        return self._member_controller.create_member(data)

    def show_member(self, member: dict):
        print("Member profile: ")
        print("email :", member['email'], " et pseudo : ", member['pseudo'])
        print("mot_de_passe:", member['mot_de_passe'])
        print("genre:", member['genre'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_members(self):
        members = self._member_controller.list_members()

        print("Members: ")
        for member in members:
            print("* %s %s (%s)" % (   member['email'],
                                            member['pseudo'],
                                            member['genre']))

    def search_member(self):
        print("ahh")
        email = self._common.ask_email('email')
        print("oui")
        member = self._member_controller.search_member(email)
        self.show_member(member)
        return member

    # À faire ! Revoir la fonction des musiques
    '''def update_member(self):
        member = self.search_member()
        data = {}
        print("Update Member")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        data['type'] = self._common.ask_type(default=member['type'])
        print()
        return self._member_controller.update_member(member['id'], data)'''

    def delete_member(self):
        member = self.search_member()
        self._member_controller.delete_member(member['id'])
        self.succes_message()
