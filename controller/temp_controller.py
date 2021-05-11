class TempController:
    def __init__(self, member_controller, music_controller):
        #On récupère les 2 controlleurs pour plus de simplicité
        self._member_controller = member_controller
        self._music_controller = music_controller

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
        for element in liste_informations:
            possible_musique = self._music_controller.search_music_title(element)
            if possible_musique != None:
                musiques.append(possible_musique)
        possible_musique = self._music_controller.search_music_title(data)
        if possible_musique != None:
            musiques.append(possible_musique)
        if musiques == []:
            return None
        return musiques