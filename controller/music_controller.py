import re

from model.dao.music_dao import MusicDAO
from exceptions import Error, InvalidData

import sys
from os import listdir
from os.path import join, isdir


class MusicController:
    """
    Music actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_musics(self):
        with self._database_engine.new_session() as session:
            musics = MusicDAO(session).get_all()
            musics_data = [music.to_dict() for music in musics]
        return musics_data

    def get_music(self, music_id):
        with self._database_engine.new_session() as session:
            music = MusicDAO(session).get(music_id)
            music_data = music.to_dict()
        return music_data

    def get_artiste(self, data):
        with self._database_engine.new_session() as session:
            artiste = MusicDAO(session).get_by_artiste(data)
            if artiste != None and artiste != []:
                return data
            return None

    def create_music(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save music in database
                music = MusicDAO(session).create(data)
                music_data = music.to_dict()
                return music_data
        except Error as e:
            # log error
            raise e

    def update_music(self, music_id, music_data):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get(music_id)
            music = music_dao.update(music, music_data)
            return music.to_dict()

    def delete_music(self, music_id):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get(music_id)
            music_dao.delete(music)

    def search_music(self, titre, artiste, album):
        # Query database
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get_by_titre_artiste_album(titre, artiste, album)
            if music == None:
                return None
            return music.to_dict()

    def search_music_title(self, titre):
        # Query database
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get_by_titre(titre)
            if music == None:
                return None
            return music.to_dict()

    def ajout_stream_music(self, musique_id):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            music = music_dao.get(musique_id)
            music_dao.ajout_stream(music)

    def get_top_musics(self):
        with self._database_engine.new_session() as session:
            music_dao = MusicDAO(session)
            musiques = music_dao.get_top()
            liste_musiques = []
            for musique in musiques:
                liste_musiques.append(musique.to_dict())
            if liste_musiques == []:
                return None
            return liste_musiques

    def reinitialisation_de_la_base_de_donnees(self):
        musiques = self.list_musics()
        tableau_des_id = []
        for musique in musiques:
            id = musique['id']
            tableau_des_id.append(id)
        for id in tableau_des_id:
            self.delete_music(id)


    def initialisation_de_la_base_de_donnees(self):

        #A NOTER QUE L'ARBORESCENCE DOIT RESPECTER LA LOGIQUE DECRITE DANS LE README
        #ET LES IMAGES DOIVENT ETRE EN JPG ET LES MUSIQUES EN OGG MONO

        ###
        # Réinitialisation de l'ancienne table contenant les musiques pour en réecrire une nouvelle
        ###

        #ATTENTION
        #EN UTIILISANT CETTE FONCTION, NE PAS DEMARRER LE LOGICIEL, CAR CELA NE PEUT PAS FONCTIONNER SANS MUSIQUES
        #ATTENTION
        #IL FAUT EGALEMENT VIDER LA TABLE DE DONNEES COMPORTANT LES MUSIQUES LIKEES PAR LES UTILISATEURS
        #CECI EST DONC FAIT DANS LA FONCTION QUI APPELLE CETTE FONCTION EN PARALLELE

        self.reinitialisation_de_la_base_de_donnees()

        ###
        # Maintenant on va lire tous les fichiers des répertoires de musiques, et les re-écrire dans la table de données
        ###

        #On récupère le repertoire de musique
        monRepertoire = "support/Musique"

        #Premièrement, on parcours les répertoires des artistes
        artistes = [f for f in listdir(monRepertoire) if isdir(join(monRepertoire, f))]

        #Puis on parcours les répertoires des albums de chaque artiste
        albums = []

        for rep in artistes:
            nouvelle_liste = [f for f in listdir(join(monRepertoire, rep))]
            nouvelle_liste.append(rep)
            albums.append(nouvelle_liste)

        #Et enfin, on ajoute tout ceci dans un fichier, en prenant le soin de prendre les images / musiques / et le fichier de description
        couples = []
        for album in albums:
            for i in range(len(album) - 1):
                chemin = join(monRepertoire, album[-1], album[i])
                final = [chemin, album[-1], album[i]]
                final.append([f for f in listdir(chemin)])
                lignes = self.lire_fichier_description(chemin)
                type = lignes[0]
                final.append(type)
                couples.append(final)


        #Puis, on va séparer chacune des musiques pour que cela ait la forme suivante
        # [ titre_de_la_musique, nom_de_l'artiste, nom_de_l'album, type_de_musique, chemin_musique, chemin_cover_image ]
        # C'est extrêmement important de respecter tout ça pour le bon respect de la base de données
        musiques = []

        for couple in couples:
            fichier_image = ""
            for fichier in couple[3]:
                if (fichier[-4:] == ".jpg"):
                    fichier_image = join(couple[0], fichier)
            for fichier in couple[3]:
                if (fichier[-4:] == ".ogg"):
                    chemin_fichier = join(couple[0], fichier)
                    titre = ""
                    for i in range(len(chemin_fichier) - 5, 0, -1):
                        if chemin_fichier[i] == "/" or chemin_fichier[i] == "\\":
                            break
                        else:
                            titre += chemin_fichier[i]

                    titre = self.inverser_string(titre)

                    musiques.append([titre, couple[1], couple[2], couple[4], join(couple[0], fichier), fichier_image])

        #Le tri est enfin opérationnel, il ne reste "plus" qu'à créer les musiques correspondantes à tout ceci
        #Et on aura enfin automatiser la création des musiques
        return musiques

    def inverser_string(self, chaine):
        nouvelle_chaine = ""
        for i in range(len(chaine) - 1, -1, -1):
            nouvelle_chaine += chaine[i]
        return nouvelle_chaine

    def lire_fichier_description(self, chemin):
        fichier = open(chemin + "/description.txt", "r")
        lignes = fichier.readlines()
        return lignes