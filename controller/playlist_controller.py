class Playlistcontroller:
    """
    Playlist actions
    """

    def __init__(self, music_controller):
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
            nouvelle_playlist = Playlist(playlist, liste_id_musiques, self._music_controller)
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

class Playlist():
    def __init__(self, nom, liste_id, music_controller):
        self._music_controller = music_controller
        self.nom = nom
        self.liste_id = liste_id
        self.nombre_ecoutes = 0
        self.chemin_image = ""
        self.musiques_objet = None
        self.musiques = self.creation()


    def creation(self):
        self.musiques_objet = self._music_controller.list_musics()
        musiques = []
        for i in range(len(self.liste_id)):
            # On va repérer les musiques grâce à leur titre, leur artiste, leur id et leur id dans la playlist
            musique_dans_playlist = {}
            for musique in self.musiques_objet:
                if self.liste_id[i] == musique['id']:
                    self.nombre_ecoutes += musique['stream']
                    self.chemin_image = musique['chemin_cover_image']
                    self.artiste = musique['artiste']
                    musique_dans_playlist = {"titre": musique['titre'], 'artiste': musique['artiste'], 'id': musique['id'], 'id_dans_playlist': i}
            musiques.append(musique_dans_playlist)
        self.nombres_musiques = len(musiques)
        return musiques

    def actualisation(self):
        self.musiques_objet = self._music_controller.list_musics()
        self.nombre_ecoutes = 0
        for musique in self.musiques:
            id = musique['id']
            for musique_ in self.musiques_objet:
                if musique_['id'] == id:
                    self.nombre_ecoutes += musique_['stream']