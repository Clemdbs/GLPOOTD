from controller.playlist_controller import Playlistcontroller
from controller.session_active_controller import Session

class TempController:
    def __init__(self, member_controller, music_controller, music_like_controller):
        #On récupère les 2 controlleurs pour plus de simplicité
        self._session_controller = Session()
        self._member_controller = member_controller
        self._music_controller = music_controller
        self._music_like_controller = music_like_controller
        self._playlist_controller = Playlistcontroller(self._music_controller, self._session_controller, music_like_controller)

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
                self._session_controller.initialiser_user(member['id'], member['pseudo'])
                return member
            else:
                return None

    def add_music_like(self):
        if self._session_controller.id_user != "" and self._session_controller.id_musique_en_cours != "":
            self._music_like_controller.create_music_like({"id_musique":self._session_controller.id_musique_en_cours, "id_utilisateur":self._session_controller.id_user})
            return self.get_playlist_like()
        return None

    def delete_music_like(self):
        if self._session_controller.id_user != "" and self._session_controller.id_musique_en_cours != "":
            musique = self._music_like_controller.get_id_by_data(
                {"id_musique": self._session_controller.id_musique_en_cours,
                 "id_utilisateur": self._session_controller.id_user})
            if musique == None:
                return None
            self._music_like_controller.delete_music(musique['id'])
            return self.get_playlist_like()
        return None

    def islike(self):
        if self._session_controller.id_user != "" and self._session_controller.id_musique_en_cours != "":
            data = {"id_musique": self._session_controller.id_musique_en_cours, "id_utilisateur": self._session_controller.id_user}
            print(data, "data")
            retour = self._music_like_controller.get_id_by_data(data)
            print(retour)
            if retour == None:
                return False
            print("oui")
            return True

    def get_playlist_like(self):
        playlist = self._playlist_controller.playlist_perso()
        return playlist


    def recherche_musique_ou_artiste(self, data):
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
            self.lecture_musique(possible_musique)
            musiques.append(possible_musique)
        for element in liste_informations:
            possible_musique = self._music_controller.search_music_title(element)
            if possible_musique != None:
                musiques.append(possible_musique)
        if musiques == []:
            # On essaie de voir s'il ne s'agit pas d'un artiste
            artiste = self._music_controller.get_artiste(data)
            if artiste != None:
                print(artiste, "testaussi")
                return artiste
            return None
        print("test_fin_de_fonction")
        return musiques

    #Fonction temporaire
    def lecture_musique(self, musique):
        self._session_controller.actualiser_musique(musique['id'])
        self._music_controller.ajout_stream_music(musique['id'])
        print(self._session_controller.id_musique_en_cours)

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

    def retour_user(self):
        user = self._session_controller.id_user
        return user
