class Music_LikeVue:
    """
    Music_Like Vue
    Musics Like interface features
    """

    def __init__(self, music_like_controller):
        self._music_like_controller = music_like_controller

    def add_music_like(self, informations):
        data = {}
        print("Information musique :")
        print(informations)
        print()
        data['id_musique'] = informations[0]
        data['id_utilisateur'] = informations[1]
        return self._music_like_controller.create_music_like(data)

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_musics(self):
        musics = self._music_like_controller.list_musics_like()
        print("Musiques : ")
        for music in musics:
            print("* %s %s" % (   music['id_musique'],
                                            music['id_utilisateur']))