from controller.session_active_controller import Session

class Playlistcontroller:
    """
    Playlist actions
    """

    def __init__(self, music_controller, session_controller, music_like_controller):
        self._music_like_controller = music_like_controller
        self._session_controller = session_controller
        self._music_controller = music_controller
        self.liste_nom_playliste = ""
        self.liste_playlists = []
        self.creation_playlist()

    def creation_playlist(self):
        liste_musiques = self._music_controller.list_musics()
        liste_nom_playlists = []
        #Ici, on crée toutes les playlists albums (juste les noms pour l'instant)
        for musique in liste_musiques:
            if musique['album'] not in liste_nom_playlists:
                liste_nom_playlists.append(musique['album'])
        #Puis on va crée les vrais objets playlist
        liste_playlists = []
        for playlist in liste_nom_playlists:
            liste_id_musiques = []
            for musique in liste_musiques:
                if musique['album'] == playlist:
                    liste_id_musiques.append(musique['id'])
            nouvelle_playlist = Playlist(playlist, liste_id_musiques, self._music_controller, "universelle", self._music_like_controller, self._session_controller)
            liste_playlists.append(nouvelle_playlist)
        self.liste_playlists = liste_playlists
        self.liste_nom_playliste = liste_nom_playlists

    def get_playlist_by_musique_id(self, musique_id):
        for playlist in self.liste_playlists:
            for musique in playlist.musiques:
                if musique['id'] == musique_id:
                    return playlist

    def get_id_musique_dans_playlist_in_playlist(self, musique_id, playlist):
        for musique in playlist.musiques:
            if musique['id'] == musique_id:
                return musique['id_dans_playlist']

    def get_id_musique_in_playlist(self, musique_id_in_playlist, playlist):
        for musique in playlist.musiques:
            if musique['id_dans_playlist'] == musique_id_in_playlist:
                return musique['id']

    def get_top_albums(self):
        temp = self.liste_playlists
        #Ici on actualise les streams de l'album pour que l'affichage s'actualise
        for album in temp:
            self.actualisation_ecoutes(album)
        top_sauvegarde = {'nom': "", 'liste_id': [], 'nombre_ecoutes': 0, "artiste": ""}
        sauvegarde = []
        top3 = []
        for i in range(3):
            album_a_supp = None
            top = {'nom': "", 'liste_id': [], 'nombre_ecoutes': 0, "artiste": ""}
            for album in temp:
                if album.nombre_ecoutes > top['nombre_ecoutes']:
                    album_a_supp = album
                    top = {'nom': album.nom, 'liste_id': album.liste_id, 'nombre_ecoutes': album.nombre_ecoutes, 'chemin_image': album.chemin_image, "artiste": album.artiste}
            top3.append(top)
            if album_a_supp != None:
                temp.remove(album_a_supp)
                sauvegarde.append(album_a_supp)
        #Ici on met ça pour éviter de supprimer les éléments de la liste_playlists
        #C'est une sorte de pointeur
        self.liste_playlists += sauvegarde
        #Maintenant, on parcours la liste (de longueur 3), et on supprime tous les éléments égaux à top
        test = True
        while test:
            for top_ in top3:
                if top_ == top_sauvegarde:
                    top3.remove(top_)
                    break
            if top_sauvegarde not in top3:
                test = False
        #Une fois que le top est cohérent, on le retourne
        return top3

    def get_albums(self, artiste):
        liste_albums = []
        for album in self.liste_playlists:
            if album.artiste == artiste:
                liste_albums.append(album)
        return liste_albums

    #Fonction pour actualiser le nombre d'écoutes de l'album
    def actualisation_ecoutes(self, album):
        album.actualisation()

    def playlist_perso(self):
        nouvelle_playlist = Playlist("Playlist des musiques likées", None, self._music_controller, "personnelle", self._music_like_controller, self._session_controller)
        return nouvelle_playlist

class Playlist():
    def __init__(self, nom, liste_id, _music_controller, test, music_like_controller, session_controller):
        self._session_controller = session_controller
        self._music_like_controller = music_like_controller
        self._music_controller = _music_controller
        self.nom = nom
        self.liste_id = liste_id
        self.nombre_ecoutes = 0
        self.chemin_image = ""
        self.musiques_objet = None
        self.musiques_ = []
        if test == "universelle":
            self.musiques = self.creation()
        else:
            self.actualisation_playlist_musiques_like()


    def creation(self):
        self.musiques_objet = self._music_controller.list_musics()
        musiques = []
        for i in range(len(self.liste_id)):
            # On va repérer les musiques grâce à leur titre, leur artiste, leur id et leur id dans la playlist
            musique_dans_playlist = {}
            for musique in self.musiques_objet:
                if self.liste_id[i] == musique['id']:
                    self.musiques_.append(musique)
                    self.nombre_ecoutes += musique['stream']
                    self.chemin_image = musique['chemin_cover_image']
                    self.artiste = musique['artiste']
                    musique_dans_playlist = {"titre": musique['titre'], 'artiste': musique['artiste'], 'id': musique['id'], 'id_dans_playlist': i}
            musiques.append(musique_dans_playlist)
        self.nombres_musiques = len(musiques)
        return musiques

    def actualisation_playlist_musiques_like(self):
        id_user = self._session_controller.id_user
        self.musiques_ = []
        musiques_id = self._music_like_controller.get_id_musiques_like_by_user(id_user)
        musiques = []
        for musique_id in musiques_id:
            self.musiques_.append(self._music_controller.get_music(musique_id['id_musique']))
            musiques.append(self._music_controller.get_music(musique_id['id_musique']))
        #petit test
        for musique in musiques:
            print(musique['titre'])
        self.musiques = musiques
        self.top()

    def top(self):
        artistes = []
        for musique in self.musiques:
            test = False
            for artiste in artistes:
                if artiste['nom'] == musique['artiste']:
                    artiste['nombre_likes'] += 1
                    test = True
            if not test:
                artistes.append({"nom": musique['artiste'], "nombre_likes": 1})
        top3 = []
        if len(artistes) >= 3:
            for i in range(3):
                max = ["", 0]
                for artiste in artistes:
                    if artiste['nombre_likes'] > max[1]:
                        max[1] = artiste['nombre_likes']
                        max[0] = artiste['nom']
                top3.append({"nom": max[0], "nombre_likes": max[1]})
                artistes.remove({"nom": max[0], "nombre_likes": max[1]})
        else:
            for i in range(len(artistes)):
                max = ["", 0]
                for artiste in artistes:
                    if artiste['nombre_likes'] > max[1]:
                        max[1] = artiste['nombre_likes']
                        max[0] = artiste['nom']
                top3.append({"nom": max[0], "nombre_likes": max[1]})
                artistes.remove({"nom": max[0], "nombre_likes": max[1]})
        print(top3)
        self.top_artistes = top3


    def actualisation(self):
        self.musiques_objet = self._music_controller.list_musics()
        self.musiques_ = []
        self.nombre_ecoutes = 0
        for musique in self.musiques:
            id = musique['id']
            for musique_ in self.musiques_objet:
                if musique_['id'] == id:
                    self.musiques_.append(musique_)
                    self.nombre_ecoutes += musique_['stream']