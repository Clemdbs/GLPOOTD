from controller.playlist_controller import Playlistcontroller

class TempController:
    def __init__(self, member_controller, music_controller):
        #On récupère les 2 controlleurs pour plus de simplicité
        self._member_controller = member_controller
        self._music_controller = music_controller
        self._playlist_controller = Playlistcontroller(self._music_controller)

    def test_connection(self, data):
        #On retourne "None" dans le cas où l'utilisateur est introuvable ou si le mot de passe est faux
        #Sinon, alors on retourne le membre
        email = data[0]
        mot_de_passe = data[1]
        member = self._member_controller.search_member(email)

        if member == None:
            return None
        else:
            if (self._member_controller.connection(email, mot_de_passe)):
                return member
            else:
                return None

    def recherche_musique(self, data):
        if data == "":
            return None
        #À ce moment là, on ne sait pas si data est un titre, un artiste ou un album
        #On va le split suivant ses espaces et on va afficher toutes les possibilités dans le vue
        liste_informations = data.split(" ")
        #Au début, on va faire en fonction des titres, c'est à dire, ressortir une musique
        #Plus tard, faire avec les albums et artistes
        musiques = []
        possible_musique = self._music_controller.search_music_title(data)
        if possible_musique != None:
            # Ici, on ajoute 1 stream à la musique (plus tard on fera ça plus proprement)
            self._music_controller.ajout_stream_music(possible_musique['id'])
            musiques.append(possible_musique)
        for element in liste_informations:
            possible_musique = self._music_controller.search_music_title(element)
            if possible_musique != None:
                musiques.append(possible_musique)
        if musiques == []:
            return None
        return musiques

    #Fonction temporaire
    def lecture_musique(self, musique):
        self._music_controller.ajout_stream_music(musique['id'])

    def change_musique(self, test, id):
        playlist = self._playlist_controller.get_playlist_by_musique_id(id)
        id_dans_playlist = self._playlist_controller.get_id_musique_dans_playlist_in_playlist(id, playlist)
        # dans le cas du clic sur la flèche de gauche :
        if test == 0:
            if(id_dans_playlist > 0):
                #On récupère la musique qui a un id -1 de la musique initiale
                id_dans_playlist -= 1
            else:
                id_dans_playlist = playlist.nombres_musiques-1
        # dans l'autre cas :
        else:
            if (id_dans_playlist < playlist.nombres_musiques - 1):
                # On récupère la musique qui a un id -1 de la musique initiale
                id_dans_playlist += 1
            else:
                id_dans_playlist = 0
        nouvel_id = self._playlist_controller.get_id_musique_in_playlist(id_dans_playlist, playlist)
        # On récupère enfin la musique
        musique = self._music_controller.get_music(nouvel_id)
        return musique
