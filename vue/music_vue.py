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
        data['chemin_cover_image'] = informations[5]
        return self._music_controller.create_music(data)

    def show_music(self, music: dict):
        print("Description de la musique: ")
        print("Titre :", music['titre'], " et artiste : ", music['artiste'])
        print("album:", music['album'])
        print("type:", music['type'])
        print("Chemin image", music['chemin_cover_image'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_musics(self):
        musics = self._music_controller.list_musics()
        print("Musiques : ")
        for music in musics:
            print("* %s %s (%s) - %s %s, %s" % (   music['titre'],
                                            music['artiste'],
                                            music['album'],
                                            music['stream'],
                                            music['id'],
                                            music['chemin_musique']))

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