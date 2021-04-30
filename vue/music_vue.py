from vue.common_music import Common_music

class MusicVue:
    """
    Music Vue
    Musics interface features
    """

    def __init__(self, music_controller):
        self._music_controller = music_controller
        self._common = Common_music()

    def add_music(self, informations):
        data = {}
        print("Information musique :")
        print(informations)
        print()
        data['titre'] = informations[0]
        data['artiste'] = informations[1]
        data['album'] = informations[2]
        data['type'] = informations[3]
        data['chemin_musique'] = informations[4]
        data['chemin_cover_image'] = informations[4]
        return self._music_controller.create_music(data)

    def show_music(self, music: dict):
        print("Description de la musique: ")
        print("Titre :", music['titre'], " et artiste : ", music['artiste'])
        print("album:", music['album'])
        print("type:", music['type'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_musics(self):
        musics = self._music_controller.list_musics()
        print("Musiques : ")
        for music in musics:
            print("* %s %s (%s) - %s %s" % (   music['titre'],
                                            music['artiste'],
                                            music['album'],
                                            music['stream'],
                                            music['id']))

    def search_music(self):
        titre = self._common.ask_titre('titre')
        artiste = self._common.ask_artiste('artiste')
        album = self._common.ask_album('album')
        music = self._music_controller.search_music(titre, artiste, album)
        self.show_music(music)
        return music

    def delete_music(self, titre, artiste, album):
        print(titre)
        print(artiste)
        print(album)
        music = self._music_controller.search_music(titre, artiste, album)
        self.show_music(music)
        self._music_controller.delete_music(music['id'])
        self.succes_message()

#A FAIRE
'''
    def update_member(self):
        member = self.search_member()
        data = {}
        print("Update Member")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        data['type'] = self._common.ask_type(default=member['type'])
        print()
        return self._member_controller.update_member(member['id'], data)
'''

