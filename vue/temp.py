import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider, QApplication
from PyQt5.QtCore import Qt, QSize

from vue.member_vue import MemberVue
from vue.music_vue import MusicVue
from vue.music_like_vue import Music_LikeVue

from controller.temp_controller import TempController
# Pour la musique
import pygame
import mutagen
import time


class Ui_Dialog:
    def __init__(self, member_controller, music_controller, music_like_controller):
        self._member_controller = member_controller
        self._member_vue = MemberVue(self._member_controller)

        self._music_controller = music_controller
        self._music_vue = MusicVue(self._music_controller)

        self._music_like_controller = music_like_controller
        self._music_like_vue = Music_LikeVue(self._music_like_controller)

        self._temp_controller = TempController(self._member_controller, self._music_controller,
                                               self._music_like_controller)
        self._playlist_controller = self._temp_controller._playlist_controller

        # Initialiser le pygame (pour le son une nouvelle fois)
        pygame.init()
        self.id = None
        self.initialisation_pygame_mixer()

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)

        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.stackedWidget.setObjectName("stackedWidget")

        ##-------------------------------------------------------------
        # PAGE D'ACCUEIL (après connexion)
        ##-------------------------------------------------------------

        self.Interface_accueil = QtWidgets.QWidget()
        self.Interface_accueil.setObjectName("Interface_accueil")
        self.widget_5 = QtWidgets.QWidget(self.Interface_accueil)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_5.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_Accueil_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Accueil_1.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_1.setFont(font)
        self.pushButton_Accueil_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_1.setCheckable(False)
        self.pushButton_Accueil_1.setAutoRepeat(False)
        self.pushButton_Accueil_1.setAutoExclusive(False)
        self.pushButton_Accueil_1.setFlat(True)
        self.pushButton_Accueil_1.setObjectName("pushButton_Accueil_1")
        self.pushButton_Recherche_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Recherche_1.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_1.setFont(font)
        self.pushButton_Recherche_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_1.setCheckable(False)
        self.pushButton_Recherche_1.setAutoRepeat(False)
        self.pushButton_Recherche_1.setAutoExclusive(False)
        self.pushButton_Recherche_1.setFlat(True)
        self.pushButton_Recherche_1.setObjectName("pushButton_Recherche_1")
        self.pushButton_Compte_1 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_Compte_1.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_1.setFont(font)
        self.pushButton_Compte_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_1.setCheckable(False)
        self.pushButton_Compte_1.setAutoRepeat(False)
        self.pushButton_Compte_1.setAutoExclusive(False)
        self.pushButton_Compte_1.setFlat(True)
        self.pushButton_Compte_1.setObjectName("pushButton_Compte_1")

        self.label_cover_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_cover_1.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_1.setText("")
        self.label_cover_1.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_1.setScaledContents(True)
        self.label_cover_1.setObjectName("label_cover_1")

        self.pushButton_gauche_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_gauche_1.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_1.setText("")
        icon_gauche = QtGui.QIcon()
        icon_gauche.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_gauche.ico"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        self.pushButton_gauche_1.setIcon(icon_gauche)
        self.pushButton_gauche_1.setObjectName("pushButton_gauche_1")
        self.pushButton_droite_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_droite_1.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_1.setText("")
        icon_droite = QtGui.QIcon()
        icon_droite.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_droite.ico"), QtGui.QIcon.Normal,
                              QtGui.QIcon.Off)
        self.pushButton_droite_1.setIcon(icon_droite)
        self.pushButton_droite_1.setObjectName("pushButton_droite_1")

        self.temps_1 = QSlider(Qt.Horizontal, self.Interface_accueil)
        self.temps_1.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.temps_1.setMinimum(0)
        self.temps_1.setMaximum(100)
        self.temps_1.setValue(50)

        self.volume_1 = QSlider(Qt.Horizontal, self.Interface_accueil)
        self.volume_1.setGeometry(QtCore.QRect(40, 530, 151, 17))
        self.volume_1.setMinimum(0)
        self.volume_1.setMaximum(100)
        self.volume_1.setValue(50)

        self.pushButton_pause_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_pause_1.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_1.setText("")
        self.icon_pause = QtGui.QIcon()
        self.icon_pause.addPixmap(QtGui.QPixmap(r"support\Interface\pause.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_play = QtGui.QIcon()
        self.icon_play.addPixmap(QtGui.QPixmap(r"support\Interface\play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pause_1.setIcon(self.icon_pause)
        self.pushButton_pause_1.setObjectName("pushButton_pause_1")

        self.pushButton_coeur_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_coeur_1.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_1.setText("")
        self.icon_coeur_vide = QtGui.QIcon()
        self.icon_coeur_vide.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_vide.ico"), QtGui.QIcon.Normal,
                                       QtGui.QIcon.Off)
        self.icon_coeur_plein = QtGui.QIcon()
        self.icon_coeur_plein.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_plein.ico"), QtGui.QIcon.Normal,
                                        QtGui.QIcon.Off)
        self.couleur = "noir"

        self.pushButton_coeur_1.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_1.setObjectName("pushButton_coeur_1")
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_1.setStyleSheet("border-style:outset")

        self.nom_musique_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.nom_musique_1.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.nom_artiste_1.setGeometry(QtCore.QRect(40, 415, 151, 30))
        self.nom_artiste_1.setStyleSheet("color: rgb(255, 255, 255); text-align: left")
        self.nom_artiste_1.setCheckable(False)
        self.nom_artiste_1.setAutoRepeat(False)
        self.nom_artiste_1.setAutoExclusive(False)
        self.nom_artiste_1.setFlat(True)
        self.nom_artiste_1.setObjectName("nom_artiste_1")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_musique_1.setFont(font)
        font2 = QtGui.QFont()
        font2.setBold(True)
        font2.setWeight(50)
        self.nom_artiste_1.setFont(font2)

        self.pushButton_4 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 50, 80, 80))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        # Label pour le titre de l'album et le nom de l'artiste lié à l'album
        self.label_top_playlist1_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.label_top_playlist1_1.setGeometry(QtCore.QRect(250, 140, 200, 80))
        self.label_top_playlist1_1.setCheckable(False)
        self.label_top_playlist1_1.setAutoRepeat(False)
        self.label_top_playlist1_1.setAutoExclusive(False)
        self.label_top_playlist1_1.setFlat(True)
        self.label_top_playlist1_1.setStyleSheet("text-align: left")
        # Label pour indiquer le nombre de streams de cet album :
        self.label_top_playlist1_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_playlist1_2.setGeometry(QtCore.QRect(250, 210, 161, 31))
        self.label_top_playlist1_2.setText("")
        self.label_playlists_populaires = QtWidgets.QLabel(self.Interface_accueil)
        self.label_playlists_populaires.setGeometry(QtCore.QRect(250, 20, 300, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_playlists_populaires.setFont(font)
        self.label_playlists_populaires.setObjectName("label_playlists_populaires")
        self.pushButton_5 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 50, 80, 80))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setAcceptDrops(False)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        # Label pour le titre de l'album et le nom de l'artiste lié à l'album
        self.label_top_playlist2_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.label_top_playlist2_1.setGeometry(QtCore.QRect(390, 140, 200, 80))
        self.label_top_playlist2_1.setCheckable(False)
        self.label_top_playlist2_1.setAutoRepeat(False)
        self.label_top_playlist2_1.setAutoExclusive(False)
        self.label_top_playlist2_1.setFlat(True)
        self.label_top_playlist2_1.setStyleSheet("text-align: left")
        # Label pour indiquer le nombre de streams de cet album :
        self.label_top_playlist2_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_playlist2_2.setGeometry(QtCore.QRect(390, 210, 161, 31))
        self.label_top_playlist2_2.setText("")
        self.label_musiques_populaires = QtWidgets.QLabel(self.Interface_accueil)
        self.label_musiques_populaires.setGeometry(QtCore.QRect(250, 245, 300, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_musiques_populaires.setFont(font)
        self.label_musiques_populaires.setObjectName("label_musiques_populaires")
        self.pushButton_8 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(250, 275, 80, 80))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setAcceptDrops(False)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setText("")
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        # Label pour le titre de la musique et le nom de l'artiste lié à la musique
        self.label_top_musique1_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique1_1.setGeometry(QtCore.QRect(250, 365, 200, 80))
        self.label_top_musique1_1.setText("")
        # Label pour indiquer le nombre de streams de cette musique :
        self.label_top_musique1_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique1_2.setGeometry(QtCore.QRect(250, 435, 161, 31))
        self.label_top_musique1_2.setText("")
        self.pushButton_9 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 275, 80, 80))
        self.pushButton_9.setMouseTracking(False)
        self.pushButton_9.setAcceptDrops(False)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setText("")
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        # Label pour le titre de la musique et le nom de l'artiste lié à la musique
        self.label_top_musique2_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique2_1.setGeometry(QtCore.QRect(390, 365, 200, 80))
        self.label_top_musique2_1.setText("")
        # Label pour indiquer le nombre de streams de cette musique :
        self.label_top_musique2_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique2_2.setGeometry(QtCore.QRect(390, 435, 161, 31))
        self.label_top_musique2_2.setText("")
        self.pushButton_10 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 275, 80, 80))
        self.pushButton_10.setMouseTracking(False)
        self.pushButton_10.setAcceptDrops(False)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setText("")
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        # Label pour le titre de la musique et le nom de l'artiste lié à la musique
        self.label_top_musique3_1 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique3_1.setGeometry(QtCore.QRect(530, 365, 200, 80))
        self.label_top_musique3_1.setText("")
        # Label pour indiquer le nombre de streams de cette musique :
        self.label_top_musique3_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_musique3_2.setGeometry(QtCore.QRect(530, 435, 161, 31))
        self.label_top_musique3_2.setText("")
        self.pushButton_13 = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setGeometry(QtCore.QRect(530, 50, 80, 80))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setAcceptDrops(False)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setText("")
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
        # Label pour le titre de l'album et le nom de l'artiste lié à l'album
        self.label_top_playlist3_1 = QtWidgets.QPushButton(self.Interface_accueil)
        self.label_top_playlist3_1.setGeometry(QtCore.QRect(530, 140, 200, 80))
        self.label_top_playlist3_1.setCheckable(False)
        self.label_top_playlist3_1.setAutoRepeat(False)
        self.label_top_playlist3_1.setAutoExclusive(False)
        self.label_top_playlist3_1.setFlat(True)
        self.label_top_playlist3_1.setStyleSheet("text-align: left")
        # Label pour indiquer le nombre de streams de cet album :
        self.label_top_playlist3_2 = QtWidgets.QLabel(self.Interface_accueil)
        self.label_top_playlist3_2.setGeometry(QtCore.QRect(530, 210, 161, 31))
        self.label_top_playlist3_2.setText("")

        self.label_playlist_personnelle = QtWidgets.QLabel(self.Interface_accueil)
        self.label_playlist_personnelle.setGeometry(QtCore.QRect(250, 470, 300, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_playlist_personnelle.setFont(font)
        self.label_playlist_personnelle.setObjectName("label_playlist_personnelle")
        self.label_playlist_personnelle.setText("Playlist des musiques likées")
        self.pushButton_playlist_personnelle = QtWidgets.QPushButton(self.Interface_accueil)
        self.pushButton_playlist_personnelle.setEnabled(True)
        self.pushButton_playlist_personnelle.setGeometry(QtCore.QRect(250, 500, 80, 80))
        self.pushButton_playlist_personnelle.setMouseTracking(False)
        self.pushButton_playlist_personnelle.setAcceptDrops(False)
        self.pushButton_playlist_personnelle.setAutoFillBackground(False)
        self.pushButton_playlist_personnelle.setStyleSheet("")
        self.pushButton_playlist_personnelle.setText("")
        self.pushButton_playlist_personnelle.setCheckable(False)
        self.pushButton_playlist_personnelle.setDefault(False)
        self.pushButton_playlist_personnelle.setFlat(False)
        self.pushButton_playlist_personnelle.setObjectName("pushButton_playlist_personnelle")
        self.pushButton_playlist_personnelle.setIcon(
            QtGui.QIcon(QtGui.QPixmap(r"support\Interface\playlist_personnelle.jpg")))
        self.pushButton_playlist_personnelle.setIconSize(QSize(80, 80))

        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_accueil)

        ##-------------------------------------------------------------
        ##PAGE DE RECHERCHE
        ##-------------------------------------------------------------

        self.Interface_recherche = QtWidgets.QWidget()
        self.Interface_recherche.setObjectName("Interface_recherche")
        self.widget_6 = QtWidgets.QWidget(self.Interface_recherche)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_6.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_6.setObjectName("widget_6")
        self.pushButton_Accueil_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Accueil_2.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_2.setFont(font)
        self.pushButton_Accueil_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_2.setCheckable(False)
        self.pushButton_Accueil_2.setAutoRepeat(False)
        self.pushButton_Accueil_2.setAutoExclusive(False)
        self.pushButton_Accueil_2.setFlat(True)
        self.pushButton_Accueil_2.setObjectName("pushButton_Accueil_2")
        self.pushButton_Recherche_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Recherche_2.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_2.setFont(font)
        self.pushButton_Recherche_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_2.setCheckable(False)
        self.pushButton_Recherche_2.setAutoRepeat(False)
        self.pushButton_Recherche_2.setAutoExclusive(False)
        self.pushButton_Recherche_2.setFlat(True)
        self.pushButton_Recherche_2.setObjectName("pushButton_Recherche_2")
        self.pushButton_Compte_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_Compte_2.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_2.setFont(font)
        self.pushButton_Compte_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_2.setCheckable(False)
        self.pushButton_Compte_2.setAutoRepeat(False)
        self.pushButton_Compte_2.setAutoExclusive(False)
        self.pushButton_Compte_2.setFlat(True)
        self.pushButton_Compte_2.setObjectName("pushButton_Compte_2")
        self.nom_utilisateur = QtWidgets.QLabel(self.Interface_recherche)
        self.nom_utilisateur.setGeometry(QtCore.QRect(250, 0, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nom_utilisateur.setFont(font)
        self.nom_utilisateur.setText("")
        self.nom_utilisateur.setObjectName("nom_utilisateur")
        self.label_rechercher = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher.setGeometry(QtCore.QRect(260, 100, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher.setFont(font)
        self.label_rechercher.setObjectName("label_rechercher")
        self.lineEdit_barre_de_recherche = QtWidgets.QLineEdit(self.Interface_recherche)
        self.lineEdit_barre_de_recherche.setGeometry(QtCore.QRect(260, 130, 161, 21))
        self.lineEdit_barre_de_recherche.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_barre_de_recherche.setObjectName("lineEdit_barre_de_recherche")
        self.pushButton_rechercher = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_rechercher.setGeometry(QtCore.QRect(421, 130, 31, 21))
        self.pushButton = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 80, 71))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(2, 82, 255);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"MS Shell Dlg 2\";https://www.hostinger.fr/tutoriels/commandes-git")
        self.pushButton.setCheckable(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 200, 80, 71))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 75 12pt \"MS Shell Dlg 2\";https://www.hostinger.fr/tutoriels/commandes-git")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_rechercher_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher_2.setGeometry(QtCore.QRect(260, 170, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_2.setFont(font)
        self.label_rechercher_2.setObjectName("label_rechercher_2")

        self.label_cover_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_cover_2.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_2.setText("")
        self.label_cover_2.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_2.setScaledContents(True)
        self.label_cover_2.setObjectName("label_cover_2")

        self.pushButton_gauche_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_gauche_2.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_2.setText("")
        self.pushButton_gauche_2.setIcon(icon_gauche)
        self.pushButton_gauche_2.setObjectName("pushButton_gauche_2")
        self.pushButton_droite_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_droite_2.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_2.setText("")
        self.pushButton_droite_2.setIcon(icon_droite)
        self.pushButton_droite_2.setObjectName("pushButton_droite_2")

        self.temps_2 = QSlider(Qt.Horizontal, self.Interface_recherche)
        self.temps_2.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.temps_2.setMinimum(0)
        self.temps_2.setMaximum(100)
        self.temps_2.setValue(50)

        self.volume_2 = QSlider(Qt.Horizontal, self.Interface_recherche)
        self.volume_2.setGeometry(QtCore.QRect(40, 530, 151, 17))
        self.volume_2.setMinimum(0)
        self.volume_2.setMaximum(100)
        self.volume_2.setValue(50)

        self.pushButton_pause_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_pause_2.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_2.setText("")
        self.pushButton_pause_2.setIcon(self.icon_pause)
        self.pushButton_pause_2.setObjectName("pushButton_pause_2")

        self.pushButton_coeur_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_coeur_2.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_2.setText("")

        self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_2.setObjectName("pushButton_coeur_2")
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_2.setStyleSheet("border-style:outset")

        self.nom_musique_2 = QtWidgets.QLabel(self.Interface_recherche)
        self.nom_musique_2.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_2 = QtWidgets.QPushButton(self.Interface_recherche)
        self.nom_artiste_2.setGeometry(QtCore.QRect(40, 415, 151, 30))
        self.nom_artiste_2.setStyleSheet("color: rgb(255, 255, 255); text-align: left")
        self.nom_artiste_2.setCheckable(False)
        self.nom_artiste_2.setAutoRepeat(False)
        self.nom_artiste_2.setAutoExclusive(False)
        self.nom_artiste_2.setFlat(True)
        self.nom_artiste_2.setObjectName("nom_artiste_2")
        self.nom_musique_2.setFont(font)
        self.nom_artiste_2.setFont(font2)

        self.label_rechercher_3 = QtWidgets.QLabel(self.Interface_recherche)
        self.label_rechercher_3.setGeometry(QtCore.QRect(260, 270, 171, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_rechercher_3.setFont(font)
        self.label_rechercher_3.setObjectName("label_rechercher_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 300, 80, 71))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_3.setText("")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 300, 80, 71))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setAcceptDrops(False)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(125, 255, 0, 69), stop:0.315789 rgba(64, 255, 0, 69), stop:0.423533 rgba(90, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(130, 255, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.578947 rgba(99, 255, 0, 130), stop:0.625 rgba(108, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        self.pushButton_6.setText("")
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Interface_recherche)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 300, 80, 71))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setAcceptDrops(False)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet(
            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(125, 255, 0, 69), stop:0.315789 rgba(64, 255, 0, 69), stop:0.423533 rgba(0, 207, 255, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(71, 214, 255, 130), stop:0.518717 rgba(130, 255, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.559809 rgba(71, 239, 255, 130), stop:0.578947 rgba(0, 189, 255, 130), stop:0.625 rgba(0, 251, 255, 69), stop:1 rgba(255, 255, 0, 69))")
        self.pushButton_7.setText("")
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_recherche)

        ##-------------------------------------------------------------
        ##PAGE DE COMPTE
        ##-------------------------------------------------------------

        self.Interface_compte = QtWidgets.QWidget()
        self.Interface_compte.setObjectName("Interface_compte")
        self.widget_7 = QtWidgets.QWidget(self.Interface_compte)
        self.widget_7.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_7.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_7.setObjectName("widget_7")
        self.pushButton_Accueil_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Accueil_3.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_3.setFont(font)
        self.pushButton_Accueil_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_3.setCheckable(False)
        self.pushButton_Accueil_3.setAutoRepeat(False)
        self.pushButton_Accueil_3.setAutoExclusive(False)
        self.pushButton_Accueil_3.setFlat(True)
        self.pushButton_Accueil_3.setObjectName("pushButton_Accueil_3")
        self.pushButton_Recherche_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Recherche_3.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_3.setFont(font)
        self.pushButton_Recherche_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_3.setCheckable(False)
        self.pushButton_Recherche_3.setAutoRepeat(False)
        self.pushButton_Recherche_3.setAutoExclusive(False)
        self.pushButton_Recherche_3.setFlat(True)
        self.pushButton_Recherche_3.setObjectName("pushButton_Recherche_3")
        self.pushButton_Compte_3 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_Compte_3.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_3.setFont(font)
        self.pushButton_Compte_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_3.setCheckable(False)
        self.pushButton_Compte_3.setAutoRepeat(False)
        self.pushButton_Compte_3.setAutoExclusive(False)
        self.pushButton_Compte_3.setFlat(True)
        self.pushButton_Compte_3.setObjectName("pushButton_Compte_3")

        self.label_cover_3 = QtWidgets.QLabel(self.Interface_compte)
        self.label_cover_3.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_3.setText("")
        self.label_cover_3.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_3.setScaledContents(True)
        self.label_cover_3.setObjectName("label_cover_3")

        self.pushButton_gauche_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_gauche_3.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_3.setText("")
        self.pushButton_gauche_3.setIcon(icon_gauche)
        self.pushButton_gauche_3.setObjectName("pushButton_gauche_3")
        self.pushButton_droite_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_droite_3.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_3.setText("")
        self.pushButton_droite_3.setIcon(icon_droite)
        self.pushButton_droite_3.setObjectName("pushButton_droite_3")

        self.temps_3 = QSlider(Qt.Horizontal, self.Interface_compte)
        self.temps_3.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.temps_3.setMinimum(0)
        self.temps_3.setMaximum(100)
        self.temps_3.setValue(50)

        self.volume_3 = QSlider(Qt.Horizontal, self.Interface_compte)
        self.volume_3.setGeometry(QtCore.QRect(40, 530, 151, 17))
        self.volume_3.setMinimum(0)
        self.volume_3.setMaximum(100)
        self.volume_3.setValue(50)

        self.pushButton_pause_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_pause_3.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_3.setText("")
        self.pushButton_pause_3.setIcon(self.icon_pause)
        self.pushButton_pause_3.setObjectName("pushButton_pause_3")

        self.pushButton_coeur_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_coeur_3.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_3.setText("")

        self.pushButton_coeur_3.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_3.setObjectName("pushButton_coeur_3")
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_3.setStyleSheet("border-style:outset")

        self.nom_musique_3 = QtWidgets.QLabel(self.Interface_compte)
        self.nom_musique_3.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_3 = QtWidgets.QPushButton(self.Interface_compte)
        self.nom_artiste_3.setGeometry(QtCore.QRect(40, 415, 151, 30))
        self.nom_artiste_3.setStyleSheet("color: rgb(255, 255, 255); text-align: left")
        self.nom_artiste_3.setCheckable(False)
        self.nom_artiste_3.setAutoRepeat(False)
        self.nom_artiste_3.setAutoExclusive(False)
        self.nom_artiste_3.setFlat(True)
        self.nom_artiste_3.setObjectName("nom_artiste_2")
        self.nom_musique_3.setFont(font)
        self.nom_artiste_3.setFont(font2)

        self.label_connexion_2 = QtWidgets.QLabel(self.Interface_compte)
        self.label_connexion_2.setGeometry(QtCore.QRect(260, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_connexion_2.setFont(font)
        self.label_connexion_2.setObjectName("label_connexion_2")
        self.pushButton_14 = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_14.setGeometry(QtCore.QRect(260, 150, 200, 50))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_modifier_compte = QtWidgets.QPushButton(self.Interface_compte)
        self.pushButton_modifier_compte.setGeometry(QtCore.QRect(260, 80, 200, 50))
        self.pushButton_modifier_compte.setObjectName("pushButton_modifier_compte")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_compte)

        ##-------------------------------------------------------------
        ##PAGE DE CONNEXION
        ##-------------------------------------------------------------

        self.Interface_connexion = QtWidgets.QWidget()
        self.Interface_connexion.setObjectName("Interface_connexion")
        self.label_connexion = QtWidgets.QLabel(self.Interface_connexion)
        self.label_connexion.setGeometry(QtCore.QRect(50, 70, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_connexion.setFont(font)
        self.label_connexion.setObjectName("label_connexion")
        self.lineEdit_adresse_mail_1 = QtWidgets.QLineEdit(self.Interface_connexion)
        self.lineEdit_adresse_mail_1.setGeometry(QtCore.QRect(50, 170, 201, 21))
        self.lineEdit_adresse_mail_1.setObjectName("lineEdit_adresse_mail_1")
        self.label_adresse_mail = QtWidgets.QLabel(self.Interface_connexion)
        self.label_adresse_mail.setGeometry(QtCore.QRect(50, 130, 201, 31))
        self.label_adresse_mail.setObjectName("label_adresse_mail")
        self.label_mot_de_passe = QtWidgets.QLabel(self.Interface_connexion)
        self.label_mot_de_passe.setGeometry(QtCore.QRect(50, 190, 201, 31))
        self.label_mot_de_passe.setObjectName("label_mot_de_passe")
        self.lineEdit_mot_de_passe_1 = QtWidgets.QLineEdit(self.Interface_connexion)
        self.lineEdit_mot_de_passe_1.setGeometry(QtCore.QRect(50, 230, 201, 21))
        self.lineEdit_mot_de_passe_1.setObjectName("lineEdit_mot_de_passe_1")
        self.pushButton_connexion = QtWidgets.QPushButton(self.Interface_connexion)
        self.pushButton_connexion.setGeometry(QtCore.QRect(50, 280, 111, 31))
        self.pushButton_connexion.setObjectName("pushButton_connexion")
        self.pushButton_pas_de_compte = QtWidgets.QPushButton(self.Interface_connexion)
        self.pushButton_pas_de_compte.setGeometry(QtCore.QRect(50, 370, 121, 31))
        self.pushButton_pas_de_compte.setObjectName("pushButton_pas_de_compte")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_connexion)

        ##-------------------------------------------------------------
        ##PAGE DE CREATION DE COMPTE
        ##-------------------------------------------------------------

        self.Interface_creation_compte = QtWidgets.QWidget()
        self.Interface_creation_compte.setObjectName("Interface_creation_compte")
        self.label_creation_de_compte = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_creation_de_compte.setGeometry(QtCore.QRect(50, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_creation_de_compte.setFont(font)
        self.label_creation_de_compte.setObjectName("label_creation_de_compte")
        self.label_adresse_mail_2 = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_adresse_mail_2.setGeometry(QtCore.QRect(50, 80, 201, 31))
        self.label_adresse_mail_2.setObjectName("label_adresse_mail_2")
        self.lineEdit_adresse_mail_2 = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_adresse_mail_2.setGeometry(QtCore.QRect(50, 120, 201, 21))
        self.lineEdit_adresse_mail_2.setObjectName("lineEdit_adresse_mail_2")
        self.label_pseudo = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_pseudo.setGeometry(QtCore.QRect(50, 140, 201, 31))
        self.label_pseudo.setObjectName("label_pseudo")
        self.lineEdit_pseudo = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_pseudo.setGeometry(QtCore.QRect(50, 170, 201, 21))
        self.lineEdit_pseudo.setObjectName("lineEdit_pseudo")
        self.label_mot_de_passe_2 = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_mot_de_passe_2.setGeometry(QtCore.QRect(50, 190, 201, 31))
        self.label_mot_de_passe_2.setObjectName("label_mot_de_passe_2")
        self.lineEdit_mot_de_passe_2 = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_mot_de_passe_2.setGeometry(QtCore.QRect(50, 220, 201, 21))
        self.lineEdit_mot_de_passe_2.setObjectName("lineEdit_mot_de_passe_2")
        self.label_confirmer_mot_de_passe = QtWidgets.QLabel(self.Interface_creation_compte)
        self.label_confirmer_mot_de_passe.setGeometry(QtCore.QRect(50, 240, 201, 31))
        self.label_confirmer_mot_de_passe.setObjectName("label_confirmer_mot_de_passe")
        self.lineEdit_confirmer_mot_de_passe = QtWidgets.QLineEdit(self.Interface_creation_compte)
        self.lineEdit_confirmer_mot_de_passe.setGeometry(QtCore.QRect(50, 270, 201, 21))
        self.lineEdit_confirmer_mot_de_passe.setObjectName("lineEdit_confirmer_mot_de_passe")
        self.comboBox_genre = QtWidgets.QComboBox(self.Interface_creation_compte)
        self.comboBox_genre.setGeometry(QtCore.QRect(50, 310, 81, 31))
        self.comboBox_genre.setObjectName("comboBox_genre")
        self.comboBox_genre.addItem("")
        self.comboBox_genre.addItem("")
        self.comboBox_genre.addItem("")
        self.comboBox_genre.addItem("")
        self.checkBox_accepter_les_conditions = QtWidgets.QCheckBox(self.Interface_creation_compte)
        self.checkBox_accepter_les_conditions.setGeometry(QtCore.QRect(50, 360, 281, 31))
        self.checkBox_accepter_les_conditions.setObjectName("checkBox_accepter_les_conditions")
        self.pushButton_creer_compte = QtWidgets.QPushButton(self.Interface_creation_compte)
        self.pushButton_creer_compte.setGeometry(QtCore.QRect(50, 420, 111, 31))
        self.pushButton_creer_compte.setObjectName("pushButton_creer_compte")
        self.pushButton_annuler = QtWidgets.QPushButton(self.Interface_creation_compte)
        self.pushButton_annuler.setGeometry(QtCore.QRect(170, 420, 111, 31))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_creation_compte)

        ##-------------------------------------------------------------
        ##PAGE D'ARTISTE
        ##-------------------------------------------------------------

        self.Interface_artiste = QtWidgets.QWidget()
        self.Interface_artiste.setObjectName("Interface_artiste")
        self.widget_8 = QtWidgets.QWidget(self.Interface_artiste)
        self.widget_8.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_8.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_Accueil_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_Accueil_4.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_4.setFont(font)
        self.pushButton_Accueil_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_4.setCheckable(False)
        self.pushButton_Accueil_4.setAutoRepeat(False)
        self.pushButton_Accueil_4.setAutoExclusive(False)
        self.pushButton_Accueil_4.setFlat(True)
        self.pushButton_Accueil_4.setObjectName("pushButton_Accueil_4")
        self.pushButton_Recherche_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_Recherche_4.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_4.setFont(font)
        self.pushButton_Recherche_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_4.setCheckable(False)
        self.pushButton_Recherche_4.setAutoRepeat(False)
        self.pushButton_Recherche_4.setAutoExclusive(False)
        self.pushButton_Recherche_4.setFlat(True)
        self.pushButton_Recherche_4.setObjectName("pushButton_Recherche_4")
        self.pushButton_Compte_4 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_Compte_4.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_4.setFont(font)
        self.pushButton_Compte_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_4.setCheckable(False)
        self.pushButton_Compte_4.setAutoRepeat(False)
        self.pushButton_Compte_4.setAutoExclusive(False)
        self.pushButton_Compte_4.setFlat(True)
        self.pushButton_Compte_4.setObjectName("pushButton_Compte_4")
        self.nom_artiste = QtWidgets.QLabel(self.Interface_artiste)
        self.nom_artiste.setGeometry(QtCore.QRect(250, 0, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nom_artiste.setFont(font)
        self.nom_artiste.setText("")
        self.nom_artiste.setObjectName("nom_artiste")

        self.label_cover_4 = QtWidgets.QLabel(self.Interface_artiste)
        self.label_cover_4.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_4.setText("")
        self.label_cover_4.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_4.setScaledContents(True)
        self.label_cover_4.setObjectName("label_cover_4")

        self.pushButton_gauche_4 = QtWidgets.QPushButton(self.Interface_artiste)
        self.pushButton_gauche_4.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_4.setText("")
        self.pushButton_gauche_4.setIcon(icon_gauche)
        self.pushButton_gauche_4.setObjectName("pushButton_gauche_4")
        self.pushButton_droite_4 = QtWidgets.QPushButton(self.Interface_artiste)
        self.pushButton_droite_4.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_4.setText("")
        self.pushButton_droite_4.setIcon(icon_droite)
        self.pushButton_droite_4.setObjectName("pushButton_droite_4")

        self.temps_4 = QSlider(Qt.Horizontal, self.Interface_artiste)
        self.temps_4.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.temps_4.setMinimum(0)
        self.temps_4.setMaximum(100)
        self.temps_4.setValue(50)

        self.volume_4 = QSlider(Qt.Horizontal, self.Interface_artiste)
        self.volume_4.setGeometry(QtCore.QRect(40, 530, 151, 17))
        self.volume_4.setMinimum(0)
        self.volume_4.setMaximum(100)
        self.volume_4.setValue(50)

        self.pushButton_pause_4 = QtWidgets.QPushButton(self.Interface_artiste)
        self.pushButton_pause_4.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_4.setText("")
        self.pushButton_pause_4.setIcon(self.icon_pause)
        self.pushButton_pause_4.setObjectName("pushButton_pause_4")

        self.pushButton_coeur_4 = QtWidgets.QPushButton(self.Interface_artiste)
        self.pushButton_coeur_4.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_4.setText("")

        self.pushButton_coeur_4.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_4.setObjectName("pushButton_coeur_4")
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_4.setStyleSheet("border-style:outset")

        self.nom_musique_4 = QtWidgets.QLabel(self.Interface_artiste)
        self.nom_musique_4.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_4 = QtWidgets.QLabel(self.Interface_artiste)
        self.nom_artiste_4.setGeometry(QtCore.QRect(40, 415, 151, 17))
        self.nom_artiste_4.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_musique_4.setFont(font)
        self.nom_artiste_4.setFont(font2)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Interface_artiste)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 110, 581, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(80)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_album1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album1.setObjectName("pushButton_album1")
        self.pushButton_album1.hide()
        self.verticalLayout_7.addWidget(self.pushButton_album1)
        self.pushButton_album2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album2.setObjectName("pushButton_album2")
        self.pushButton_album2.hide()
        self.verticalLayout_7.addWidget(self.pushButton_album2)
        self.pushButton_album3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album3.setObjectName("pushButton_album3")
        self.pushButton_album3.hide()
        self.verticalLayout_7.addWidget(self.pushButton_album3)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(80)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_album4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album4.setObjectName("pushButton_album4")
        self.pushButton_album4.hide()
        self.verticalLayout_6.addWidget(self.pushButton_album4)
        self.pushButton_album5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album5.setObjectName("pushButton_album5")
        self.pushButton_album5.hide()
        self.verticalLayout_6.addWidget(self.pushButton_album5)
        self.pushButton_album6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album6.setObjectName("pushButton_album6")
        self.pushButton_album6.hide()
        self.verticalLayout_6.addWidget(self.pushButton_album6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(80)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_album7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album7.setObjectName("pushButton_album7")
        self.pushButton_album7.hide()
        self.verticalLayout_5.addWidget(self.pushButton_album7)
        self.pushButton_album8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album8.setObjectName("pushButton_album8")
        self.pushButton_album8.hide()
        self.verticalLayout_5.addWidget(self.pushButton_album8)
        self.pushButton_album9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_album9.setObjectName("pushButton_album9")
        self.pushButton_album9.hide()
        self.verticalLayout_5.addWidget(self.pushButton_album9)
        self.horizontalLayout.addLayout(self.verticalLayout_5)

        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_artiste)

        ##-------------------------------------------------------------
        ##PAGE D'ALBUM
        ##-------------------------------------------------------------

        self.Interface_album = QtWidgets.QWidget()
        self.Interface_album.setObjectName("Interface_album")
        self.widget_9 = QtWidgets.QWidget(self.Interface_album)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 241, 721))
        self.widget_9.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.widget_9.setObjectName("widget_9")
        self.pushButton_Accueil_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_Accueil_5.setGeometry(QtCore.QRect(0, 50, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Accueil_5.setFont(font)
        self.pushButton_Accueil_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Accueil_5.setCheckable(False)
        self.pushButton_Accueil_5.setAutoRepeat(False)
        self.pushButton_Accueil_5.setAutoExclusive(False)
        self.pushButton_Accueil_5.setFlat(True)
        self.pushButton_Accueil_5.setObjectName("pushButton_Accueil_5")
        self.pushButton_Recherche_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_Recherche_5.setGeometry(QtCore.QRect(0, 100, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Recherche_5.setFont(font)
        self.pushButton_Recherche_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Recherche_5.setCheckable(False)
        self.pushButton_Recherche_5.setAutoRepeat(False)
        self.pushButton_Recherche_5.setAutoExclusive(False)
        self.pushButton_Recherche_5.setFlat(True)
        self.pushButton_Recherche_5.setObjectName("pushButton_Recherche_5")
        self.pushButton_Compte_5 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_Compte_5.setGeometry(QtCore.QRect(0, 150, 241, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_Compte_5.setFont(font)
        self.pushButton_Compte_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_Compte_5.setCheckable(False)
        self.pushButton_Compte_5.setAutoRepeat(False)
        self.pushButton_Compte_5.setAutoExclusive(False)
        self.pushButton_Compte_5.setFlat(True)
        self.pushButton_Compte_5.setObjectName("pushButton_Compte_5")
        self.nom_album = QtWidgets.QLabel(self.Interface_album)
        self.nom_album.setGeometry(QtCore.QRect(250, 0, 831, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.nom_album.setFont(font)
        self.nom_album.setText("")
        self.nom_album.setObjectName("nom_album")

        self.label_cover_5 = QtWidgets.QLabel(self.Interface_album)
        self.label_cover_5.setGeometry(QtCore.QRect(40, 220, 151, 151))
        self.label_cover_5.setText("")
        self.label_cover_5.setPixmap(QtGui.QPixmap(r"support\Interface\cover.jpg"))
        self.label_cover_5.setScaledContents(True)
        self.label_cover_5.setObjectName("label_cover_5")

        self.pushButton_gauche_5 = QtWidgets.QPushButton(self.Interface_album)
        self.pushButton_gauche_5.setGeometry(QtCore.QRect(40, 470, 51, 22))
        self.pushButton_gauche_5.setText("")
        self.pushButton_gauche_5.setIcon(icon_gauche)
        self.pushButton_gauche_5.setObjectName("pushButton_gauche_5")
        self.pushButton_droite_5 = QtWidgets.QPushButton(self.Interface_album)
        self.pushButton_droite_5.setGeometry(QtCore.QRect(140, 470, 51, 22))
        self.pushButton_droite_5.setText("")
        self.pushButton_droite_5.setIcon(icon_droite)
        self.pushButton_droite_5.setObjectName("pushButton_droite_5")

        self.temps_5 = QSlider(Qt.Horizontal, self.Interface_album)
        self.temps_5.setGeometry(QtCore.QRect(40, 450, 151, 17))
        self.temps_5.setMinimum(0)
        self.temps_5.setMaximum(100)
        self.temps_5.setValue(50)

        self.volume_5 = QSlider(Qt.Horizontal, self.Interface_album)
        self.volume_5.setGeometry(QtCore.QRect(40, 530, 151, 17))
        self.volume_5.setMinimum(0)
        self.volume_5.setMaximum(100)
        self.volume_5.setValue(50)

        self.pushButton_pause_5 = QtWidgets.QPushButton(self.Interface_album)
        self.pushButton_pause_5.setGeometry(QtCore.QRect(105, 470, 20, 22))
        self.pushButton_pause_5.setText("")
        self.pushButton_pause_5.setIcon(self.icon_pause)
        self.pushButton_pause_5.setObjectName("pushButton_pause_5")

        self.pushButton_coeur_5 = QtWidgets.QPushButton(self.Interface_album)
        self.pushButton_coeur_5.setGeometry(QtCore.QRect(99, 500, 31, 22))
        self.pushButton_coeur_5.setText("")

        self.pushButton_coeur_5.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_5.setObjectName("pushButton_coeur_5")
        # Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_coeur_5.setStyleSheet("border-style:outset")

        self.nom_musique_5 = QtWidgets.QLabel(self.Interface_album)
        self.nom_musique_5.setGeometry(QtCore.QRect(40, 400, 151, 17))
        self.nom_musique_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_artiste_5 = QtWidgets.QLabel(self.Interface_album)
        self.nom_artiste_5.setGeometry(QtCore.QRect(40, 415, 151, 17))
        self.nom_artiste_5.setStyleSheet("color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nom_musique_5.setFont(font)
        self.nom_artiste_5.setFont(font2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Interface_album)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 110, 581, 451))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setSpacing(80)
        self.verticalLayout_1.setObjectName("verticalLayout_7")
        self.pushButton_musique1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_musique1.setObjectName("pushButton_musique1")
        self.verticalLayout_1.addWidget(self.pushButton_musique1)
        self.pushButton_musique2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_musique2.setObjectName("pushButton_musique2")
        self.verticalLayout_1.addWidget(self.pushButton_musique2)
        self.pushButton_musique3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_musique3.setObjectName("pushButton_musique3")
        self.verticalLayout_1.addWidget(self.pushButton_musique3)
        self.pushButton_musique4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_musique4.setObjectName("pushButton_musique4")
        self.verticalLayout_1.addWidget(self.pushButton_musique4)
        self.pushButton_musique5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_musique5.setObjectName("pushButton_musique5")
        self.verticalLayout_1.addWidget(self.pushButton_musique5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_1)

        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_album)

        ##-------------------------------------------------------------
        ##PAGE DE MODIFICATION DE COMPTE
        ##-------------------------------------------------------------

        self.Interface_modification_compte = QtWidgets.QWidget()
        self.Interface_modification_compte.setObjectName("Interface_modification_compte")
        self.label_modification_de_compte = QtWidgets.QLabel(self.Interface_modification_compte)
        self.label_modification_de_compte.setGeometry(QtCore.QRect(50, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_modification_de_compte.setFont(font)
        self.label_modification_de_compte.setObjectName("label_modification_de_compte")
        self.label_mot_de_passe_3 = QtWidgets.QLabel(self.Interface_modification_compte)
        self.label_mot_de_passe_3.setGeometry(QtCore.QRect(50, 80, 301, 31))
        self.label_mot_de_passe_3.setObjectName("label_mot_de_passe_3")
        self.lineEdit_mot_de_passe_3 = QtWidgets.QLineEdit(self.Interface_modification_compte)
        self.lineEdit_mot_de_passe_3.setGeometry(QtCore.QRect(50, 120, 301, 21))
        self.lineEdit_mot_de_passe_3.setObjectName("lineEdit_mot_de_passe_3")
        self.label_mot_de_passe_4 = QtWidgets.QLabel(self.Interface_modification_compte)
        self.label_mot_de_passe_4.setGeometry(QtCore.QRect(50, 160, 301, 31))
        self.label_mot_de_passe_4.setObjectName("label_mot_de_passe_4")
        self.lineEdit_mot_de_passe_4 = QtWidgets.QLineEdit(self.Interface_modification_compte)
        self.lineEdit_mot_de_passe_4.setGeometry(QtCore.QRect(50, 200, 301, 21))
        self.lineEdit_mot_de_passe_4.setObjectName("lineEdit_mot_de_passe_4")
        self.label_mot_de_passe_5 = QtWidgets.QLabel(self.Interface_modification_compte)
        self.label_mot_de_passe_5.setGeometry(QtCore.QRect(50, 240, 301, 31))
        self.label_mot_de_passe_5.setObjectName("label_mot_de_passe_4")
        self.lineEdit_mot_de_passe_5 = QtWidgets.QLineEdit(self.Interface_modification_compte)
        self.lineEdit_mot_de_passe_5.setGeometry(QtCore.QRect(50, 280, 301, 21))
        self.lineEdit_mot_de_passe_5.setObjectName("lineEdit_mot_de_passe_4")

        # Pour que les mots de passe ne soient pas visible mais affichés avec des points :
        self.lineEdit_mot_de_passe_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_mot_de_passe_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_mot_de_passe_5.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton_valider = QtWidgets.QPushButton(self.Interface_modification_compte)
        self.pushButton_valider.setGeometry(QtCore.QRect(50, 320, 111, 31))
        self.pushButton_valider.setObjectName("pushButton_valider")

        self.pushButton_annuler_2 = QtWidgets.QPushButton(self.Interface_modification_compte)
        self.pushButton_annuler_2.setGeometry(QtCore.QRect(50, 500, 111, 31))
        self.pushButton_annuler_2.setObjectName("pushButton_supprimer_compte")

        self.pushButton_supprimer_compte = QtWidgets.QPushButton(self.Interface_modification_compte)
        self.pushButton_supprimer_compte.setGeometry(QtCore.QRect(50, 600, 200, 31))
        self.pushButton_supprimer_compte.setObjectName("pushButton_supprimer_compte")
        # On ajoute la page à toutes les pages que l'on aura
        self.stackedWidget.addWidget(self.Interface_modification_compte)

        # On creé tout ça :
        self.retranslateUi(Dialog)
        self.page_active = 3
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Appel de la fonction page qui permet de switcher de page comme son nom l'indique
        # Chaque page possède ses propres items
        # --------------------------------------------------------------------------------
        self.pushButton_Accueil_1.clicked.connect(lambda: self.page(0))
        self.pushButton_Accueil_2.clicked.connect(lambda: self.page(0))
        self.pushButton_Accueil_3.clicked.connect(lambda: self.page(0))
        # Attention, il faut recacher les boutons
        self.pushButton_Accueil_4.clicked.connect(lambda: self.page_speciale(0))
        self.pushButton_Accueil_5.clicked.connect(lambda: self.page_speciale2(0))

        self.pushButton_Recherche_1.clicked.connect(lambda: self.page(1))
        self.pushButton_Recherche_2.clicked.connect(lambda: self.page(1))
        self.pushButton_Recherche_3.clicked.connect(lambda: self.page(1))
        # Attention, il faut recacher les boutons
        self.pushButton_Recherche_4.clicked.connect(lambda: self.page_speciale(1))
        self.pushButton_Recherche_5.clicked.connect(lambda: self.page_speciale2(1))

        self.pushButton_Compte_1.clicked.connect(lambda: self.page(2))
        self.pushButton_Compte_2.clicked.connect(lambda: self.page(2))
        self.pushButton_Compte_3.clicked.connect(lambda: self.page(2))
        # Attention, il faut recacher les boutons
        self.pushButton_Compte_4.clicked.connect(lambda: self.page_speciale(2))
        self.pushButton_Compte_5.clicked.connect(lambda: self.page_speciale2(2))
        # --------------------------------------------------------------------------------

        # On cache les boutons que l'on veut pas afficher:
        self.boutton_musique_cache()

        # Si l'on se connecte, on arrive sur la page d'accueil
        self.pushButton_connexion.clicked.connect(lambda: self.page(0))
        # Si l'on appuie sur le bouton "Pas de compte", on arrive sur la page de création de compte
        self.pushButton_pas_de_compte.clicked.connect(lambda: self.page(4))
        # Si l'on appuie sur annuler, on arrive sur la page de connection
        self.pushButton_annuler.clicked.connect(lambda: self.page(3))

        # Si l'on appuie sur le bouton de deconnexion :
        self.pushButton_14.clicked.connect(lambda: self.page(3))
        # Si l'on appuie sur le bouton modifier le compte
        self.pushButton_modifier_compte.clicked.connect(lambda: self.page(8))
        # Si l'on appuie sur annuler sur la page de modification de compte :
        self.pushButton_annuler_2.clicked.connect(lambda: self.page(2))
        # Si l'on appuie sur bouton valider pour modifier le compte :
        self.pushButton_valider.clicked.connect(lambda: self.modification_de_compte())
        self.pushButton_supprimer_compte.clicked.connect(lambda: self.suppression_de_compte())

        # Ici, on va appeler la fonction qui va gérer la connection :
        self.pushButton_connexion.clicked.connect(lambda: self.connection())
        # Ici la recherche d'une musique (pour l'instant)
        self.pushButton_rechercher.clicked.connect(lambda: self.rechercher())

        # Gestion du bouton pause & play
        self.etat_musique = "Play"
        # À l'appui du bouton, on appelle la fonction toogle_etat_musique qui mettra en pause ou redémarrera la musique
        self.pushButton_pause_1.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_2.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_3.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_4.clicked.connect(lambda: self.toogle_etat_musique())
        self.pushButton_pause_5.clicked.connect(lambda: self.toogle_etat_musique())

        # Gestion du slider timer
        self.temps_1.sliderMoved.connect(lambda: self.set_timer(1))
        self.temps_2.sliderMoved.connect(lambda: self.set_timer(2))
        self.temps_3.sliderMoved.connect(lambda: self.set_timer(3))
        self.temps_4.sliderMoved.connect(lambda: self.set_timer(4))
        self.temps_5.sliderMoved.connect(lambda: self.set_timer(5))

        # Gestion du slider volume
        self.volume_1.sliderMoved.connect(lambda: self.set_volume(1))
        self.volume_2.sliderMoved.connect(lambda: self.set_volume(2))
        self.volume_3.sliderMoved.connect(lambda: self.set_volume(3))
        self.volume_4.sliderMoved.connect(lambda: self.set_volume(4))
        self.volume_5.sliderMoved.connect(lambda: self.set_volume(5))

        # Affichage des musiques top streams :
        self.affichage_top_musiques_stream()

        # Affichage des albums top streams:
        self.affichage_top_albums_stream()

        # Détection des clics sur les boutons contenant les musiques populaires :
        self.pushButton_8.clicked.connect(lambda: self.lecture_musique_top(1))
        self.pushButton_9.clicked.connect(lambda: self.lecture_musique_top(2))
        self.pushButton_10.clicked.connect(lambda: self.lecture_musique_top(3))

        # Détection des clics sur les flèches pour changer de musique :
        self.pushButton_gauche_1.clicked.connect(lambda: self.changer_musique(0, self.id))
        self.pushButton_droite_1.clicked.connect(lambda: self.changer_musique(1, self.id))
        self.pushButton_gauche_2.clicked.connect(lambda: self.changer_musique(0, self.id))
        self.pushButton_droite_2.clicked.connect(lambda: self.changer_musique(1, self.id))
        self.pushButton_gauche_3.clicked.connect(lambda: self.changer_musique(0, self.id))
        self.pushButton_droite_3.clicked.connect(lambda: self.changer_musique(1, self.id))
        self.pushButton_gauche_4.clicked.connect(lambda: self.changer_musique(0, self.id))
        self.pushButton_droite_4.clicked.connect(lambda: self.changer_musique(1, self.id))
        self.pushButton_gauche_5.clicked.connect(lambda: self.changer_musique(0, self.id))
        self.pushButton_droite_5.clicked.connect(lambda: self.changer_musique(1, self.id))

        # Détection des clics sur l'artiste pour ouvrir la page le concernant :
        self.nom_artiste_1.clicked.connect(lambda: self.page_artiste())
        self.nom_artiste_2.clicked.connect(lambda: self.page_artiste())
        self.nom_artiste_3.clicked.connect(lambda: self.page_artiste())

        # Détection des clics sur les top albums :
        self.label_top_playlist1_1.clicked.connect(lambda: self.page(5))
        self.label_top_playlist2_1.clicked.connect(lambda: self.page(6))
        self.label_top_playlist3_1.clicked.connect(lambda: self.page(7))

        # Détection des clics sur la playlists des musiques likées:
        self.pushButton_playlist_personnelle.clicked.connect(
            lambda: self.page_album(self._playlist_controller.playlist_perso()))

        # Lors de l'appuie sur le bouton like
        self.pushButton_coeur_1.clicked.connect(lambda: self.like())
        self.pushButton_coeur_2.clicked.connect(lambda: self.like())
        self.pushButton_coeur_3.clicked.connect(lambda: self.like())
        self.pushButton_coeur_4.clicked.connect(lambda: self.like())
        self.pushButton_coeur_5.clicked.connect(lambda: self.like())

        # Lors de l'appuie sur les boutons d'artiste préférés
        self.pushButton_3.clicked.connect(lambda: self.page_artiste_top(1))
        self.pushButton_6.clicked.connect(lambda: self.page_artiste_top(2))
        self.pushButton_7.clicked.connect(lambda: self.page_artiste_top(3))

        # Lors de l'appuie sur le bouton pour créer un compte
        self.pushButton_creer_compte.clicked.connect(lambda: self.cree_compte(self.Interface_creation_compte))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Spythonfy"))
        self.pushButton_Accueil_1.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_1.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_1.setText(_translate("Dialog", "Mon compte"))
        self.label_playlists_populaires.setText(_translate("Dialog", "Albums populaires"))
        self.label_musiques_populaires.setText(_translate("Dialog", "Musiques populaires"))
        self.pushButton_Accueil_2.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_2.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_2.setText(_translate("Dialog", "Mon compte"))
        self.label_rechercher.setText(_translate("Dialog", "Rechercher"))
        self.lineEdit_barre_de_recherche.setPlaceholderText("Artistes, titres")
        self.pushButton_rechercher.setText(_translate("Dialog", "Ok"))
        self.pushButton.setText(_translate("Dialog", "Rap"))
        self.pushButton_2.setText(_translate("Dialog", "Pop"))
        self.label_rechercher_2.setText(_translate("Dialog", "Vos genres préférés"))
        self.label_rechercher_3.setText(_translate("Dialog", "Vos artistes préférés"))
        self.pushButton_Accueil_3.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_3.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_3.setText(_translate("Dialog", "Mon compte"))
        self.label_connexion_2.setText(_translate("Dialog", "Mon compte :"))
        self.pushButton_14.setText(_translate("Dialog", "Se deconnecter"))
        self.pushButton_modifier_compte.setText(_translate("Dialog", "Modifier son compte"))
        self.label_connexion.setText(_translate("Dialog", "Connexion"))
        self.label_adresse_mail.setText(_translate("Dialog", "Adresse mail :"))
        self.label_mot_de_passe.setText(_translate("Dialog", "Mot de passe :"))
        self.pushButton_connexion.setText(_translate("Dialog", "Connexion"))
        self.pushButton_pas_de_compte.setText(_translate("Dialog", "Pas de compte ?"))
        self.label_creation_de_compte.setText(_translate("Dialog", "Création de compte"))
        self.label_modification_de_compte.setText(_translate("Dialog", "Modification de compte"))
        self.label_mot_de_passe_3.setText(_translate("Dialog", "Ancien mot de passe"))
        self.label_mot_de_passe_4.setText(_translate("Dialog", "Nouveau mot de passe"))
        self.label_mot_de_passe_5.setText(_translate("Dialog", "Confirmer le nouveau mot de passe"))
        self.pushButton_valider.setText(_translate("Dialog", "Valider"))
        self.pushButton_annuler_2.setText(_translate("Dialog", "Annuler"))
        self.pushButton_supprimer_compte.setText(_translate("Dialog", "Supprimer votre compte"))
        self.label_adresse_mail_2.setText(_translate("Dialog", "Adresse mail :"))
        self.label_pseudo.setText(_translate("Dialog", "Pseudo :"))
        self.label_mot_de_passe_2.setText(_translate("Dialog", "Mot de passe :"))
        self.label_confirmer_mot_de_passe.setText(_translate("Dialog", "Confirmation mot de passe :"))
        self.comboBox_genre.setItemText(0, _translate("Dialog", "Genre"))
        self.comboBox_genre.setItemText(1, _translate("Dialog", "Femme"))
        self.comboBox_genre.setItemText(2, _translate("Dialog", "Homme"))
        self.comboBox_genre.setItemText(3, _translate("Dialog", "Autre"))
        self.checkBox_accepter_les_conditions.setText(_translate("Dialog", "J\'accèpte les conditions d\'utilisation"))
        self.pushButton_creer_compte.setText(_translate("Dialog", "Créer compte "))
        self.pushButton_annuler.setText(_translate("Dialog", "Annuler"))
        self.lineEdit_mot_de_passe_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_Accueil_4.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_4.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_4.setText(_translate("Dialog", "Mon compte"))
        self.pushButton_Accueil_5.setText(_translate("Dialog", "Accueil"))
        self.pushButton_Recherche_5.setText(_translate("Dialog", "Recherche"))
        self.pushButton_Compte_5.setText(_translate("Dialog", "Mon compte"))

    def page(self, numero):
        if numero == 0:
            self.page_active = 0
            self.stackedWidget.setCurrentIndex(0)
        elif numero == 1:
            self.page_active = 1
            self.stackedWidget.setCurrentIndex(1)
        elif numero == 2:
            self.page_active = 2
            self.stackedWidget.setCurrentIndex(2)
        elif numero == 3:
            self.page_active = 3
            self.stackedWidget.setCurrentIndex(3)
        elif numero == 4:
            self.page_active = 4
            self.stackedWidget.setCurrentIndex(4)
        elif numero == 5 or numero == 6 or numero == 7:
            self.page_active = 5
            self.stackedWidget.setCurrentIndex(5)
            self.affichage_albums(numero - 4)
        elif numero == 8:
            self.page_active = 7
            self.stackedWidget.setCurrentIndex(7)

    def page_speciale(self, numero):
        self.boutton_album_cache()
        self.page(numero)

    def boutton_album_cache(self):
        # Ici, il faut recacher tous les boutons qui ont possiblement été décachés juste avant :
        self.pushButton_album1.hide()
        self.pushButton_album2.hide()
        self.pushButton_album3.hide()
        self.pushButton_album4.hide()
        self.pushButton_album5.hide()
        self.pushButton_album6.hide()
        self.pushButton_album7.hide()
        self.pushButton_album8.hide()
        self.pushButton_album9.hide()

    def boutton_musique_cache(self):
        # Ici, il faut recacher tous les boutons qui ont possiblement été décachés juste avant :
        self.pushButton_musique1.hide()
        self.pushButton_musique2.hide()
        self.pushButton_musique3.hide()
        self.pushButton_musique4.hide()
        self.pushButton_musique5.hide()

    def page_speciale2(self, numero):
        self.boutton_musique_cache()
        self.page(numero)

    def page_artiste(self):
        artiste = self.nom_artiste_1.text()
        if artiste != "":  # Si et seulement si un nom d'artiste est affiché
            self.page_active = 5
            self.stackedWidget.setCurrentIndex(5)
            self.affichage_albums_artiste(artiste)

    def page_artiste_top(self, numero):
        if numero == 1:
            artiste = self.pushButton_3.text()
        elif numero == 2:
            artiste = self.pushButton_6.text()
        else:
            artiste = self.pushButton_7.text()
        if artiste != "":
            self.page_active = 5
            self.stackedWidget.setCurrentIndex(5)
            self.affichage_albums_artiste(artiste)

    def page_album(self, album):
        self.boutton_musique_cache()

        self.nom_album.setText(album.nom)
        self.page_active = 6
        self.stackedWidget.setCurrentIndex(6)

        musiques = album.musiques_
        nombre_musiques = len(musiques)

        for i in range(nombre_musiques):
            if i == 0:
                self.pushButton_musique1.setText(musiques[i]['titre'] + " : " + str(musiques[i]['stream']) + " streams")
                self.pushButton_musique1.show()
                self.pushButton_musique1.clicked.connect(lambda: self.lire_musique(musiques[0]))
            elif i == 1:
                self.pushButton_musique2.setText(musiques[i]['titre'] + " : " + str(musiques[i]['stream']) + " streams")
                self.pushButton_musique2.show()
                self.pushButton_musique2.clicked.connect(lambda: self.lire_musique(musiques[1]))
            elif i == 2:
                self.pushButton_musique3.setText(musiques[i]['titre'] + " : " + str(musiques[i]['stream']) + " streams")
                self.pushButton_musique3.show()
                self.pushButton_musique3.clicked.connect(lambda: self.lire_musique(musiques[2]))
            elif i == 3:
                self.pushButton_musique4.setText(musiques[i]['titre'] + " : " + str(musiques[i]['stream']) + " streams")
                self.pushButton_musique4.show()
                self.pushButton_musique4.clicked.connect(lambda: self.lire_musique(musiques[3]))
            elif i == 4:
                self.pushButton_musique5.setText(musiques[i]['titre'] + " : " + str(musiques[i]['stream']) + " streams")
                self.pushButton_musique5.show()
                self.pushButton_musique5.clicked.connect(lambda: self.lire_musique(musiques[4]))

    def cree_compte(self, Dialog):
        # Si le bouton n'est pas accepté
        if not self.checkBox_accepter_les_conditions.isChecked():
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Veuillez accepter les conditions d\'utilisation pour utiliser nos services.')
            return 0
        # Puis si les mots de passe sont différents
        if self.lineEdit_mot_de_passe_2.text() != self.lineEdit_confirmer_mot_de_passe.text():
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Vos mots de passe ne correspondent pas.')

        email = self.lineEdit_adresse_mail_2.text()
        pseudo = self.lineEdit_pseudo.text()
        mot_de_passe = self.lineEdit_mot_de_passe_2.text()
        genre = self.comboBox_genre.currentText()

        print("test avant")
        member = self._member_vue.add_member([email, pseudo, mot_de_passe, genre])
        print("test après")
        if isinstance(member, str):
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage(member)

        self._member_vue.show_member(member)
        ####
        # FAIRE UN TEST POUR PAS DEUX COMPTES IDENTIQUES CAR SÛREMENT PAS GERE ICI
        ####
        self._member_vue.show_members()

    def set_heart_black(self):
        # Permet de mettre le coeur en noir à chaque nouvelle musique non aimée, c'est un reset en gros
        self.couleur = "noir"
        self.pushButton_coeur_1.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_2.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_3.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_4.setIcon(self.icon_coeur_vide)
        self.pushButton_coeur_5.setIcon(self.icon_coeur_vide)

    def set_heart_red(self):
        # Permet de mettre le coeur en noir à chaque nouvelle musique non aimée, c'est un reset en gros
        self.couleur = "rouge"
        self.pushButton_coeur_1.setIcon(self.icon_coeur_plein)
        self.pushButton_coeur_2.setIcon(self.icon_coeur_plein)
        self.pushButton_coeur_3.setIcon(self.icon_coeur_plein)
        self.pushButton_coeur_4.setIcon(self.icon_coeur_plein)
        self.pushButton_coeur_5.setIcon(self.icon_coeur_plein)

    def connection(self):
        # Petit affichage de test :
        self._member_vue.show_members()
        # Essaie de connection grâce au controller :
        Membre = self._temp_controller.test_connection(
            [self.lineEdit_adresse_mail_1.text(), self.lineEdit_mot_de_passe_1.text()])
        if Membre == None:
            print("Nom d'utilisateur ou mot de passe faux")
        else:
            self.nom_utilisateur.setText(Membre['pseudo'])
            self.affichage_artistes_preferes()

    def rechercher(self):
        # Essaie de recherche grâce au controller :
        Musique_ou_artiste = self._temp_controller.recherche_musique_ou_artiste(self.lineEdit_barre_de_recherche.text())
        if Musique_ou_artiste == None:
            print("Musique ou artiste non trouvé(e)")
        else:
            # Au début on gère pas encore les différents trucs obtenus
            # Mais un seul résultat
            # Après il faudra faire un affichage où on clique sur la musique désirée
            if isinstance(Musique_ou_artiste, str):
                self.page_active = 5
                self.stackedWidget.setCurrentIndex(5)
                self.affichage_albums_artiste(Musique_ou_artiste)
            else:
                musique = Musique_ou_artiste[0]
                self.lire_musique(musique)

    def affichage_cover_titre_artiste(self, musique):
        chemin_cover_image = musique['chemin_cover_image']

        # Bien faire attention de mettre à jour les autres pages :
        # Ici, on va modifier la pochette de la musique
        # Le nom de la musique
        # Et le nom de l'artiste

        self.label_cover_1.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
        self.nom_musique_1.setText(musique['titre'])
        self.nom_artiste_1.setText(musique['artiste'])

        self.label_cover_2.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
        self.nom_musique_2.setText(musique['titre'])
        self.nom_artiste_2.setText(musique['artiste'])

        self.label_cover_3.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
        self.nom_musique_3.setText(musique['titre'])
        self.nom_artiste_3.setText(musique['artiste'])

        self.label_cover_4.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
        self.nom_musique_4.setText(musique['titre'])
        self.nom_artiste_4.setText(musique['artiste'])

        self.label_cover_5.setPixmap(QtGui.QPixmap(r"" + chemin_cover_image))
        self.nom_musique_5.setText(musique['titre'])
        self.nom_artiste_5.setText(musique['artiste'])

    def toogle_etat_musique(self):
        # Si on appuie sur le bouton play ou pause, pour stopper ou redémarrer la musique
        if self.etat_musique == "Play":
            pygame.mixer.music.pause()
            self.etat_musique = "Pause"
            self.pushButton_pause_1.setIcon(self.icon_play)
            self.pushButton_pause_2.setIcon(self.icon_play)
            self.pushButton_pause_3.setIcon(self.icon_play)
            self.pushButton_pause_4.setIcon(self.icon_play)
            self.pushButton_pause_5.setIcon(self.icon_play)
        else:
            pygame.mixer.music.unpause()
            self.etat_musique = "Play"
            self.pushButton_pause_1.setIcon(self.icon_pause)
            self.pushButton_pause_2.setIcon(self.icon_pause)
            self.pushButton_pause_3.setIcon(self.icon_pause)
            self.pushButton_pause_4.setIcon(self.icon_pause)
            self.pushButton_pause_5.setIcon(self.icon_pause)

    def set_timer(self, numero):
        # On met à jour les sliders des autres pages en même temps que
        # de récupérer la valeur du slider de la page active.
        if numero == 1:
            valeur = self.temps_1.value()
            self.temps_2.setValue(valeur)
            self.temps_3.setValue(valeur)
            self.temps_4.setValue(valeur)
            self.temps_5.setValue(valeur)
        elif numero == 2:
            valeur = self.temps_2.value()
            self.temps_1.setValue(valeur)
            self.temps_3.setValue(valeur)
            self.temps_4.setValue(valeur)
            self.temps_5.setValue(valeur)
        elif numero == 3:
            valeur = self.temps_3.value()
            self.temps_2.setValue(valeur)
            self.temps_1.setValue(valeur)
            self.temps_4.setValue(valeur)
            self.temps_5.setValue(valeur)
        elif numero == 4:
            valeur = self.temps_4.value()
            self.temps_2.setValue(valeur)
            self.temps_1.setValue(valeur)
            self.temps_3.setValue(valeur)
            self.temps_5.setValue(valeur)
        else:
            valeur = self.temps_5.value()
            self.temps_2.setValue(valeur)
            self.temps_1.setValue(valeur)
            self.temps_3.setValue(valeur)
            self.temps_4.setValue(valeur)
        # Et on va aussi venir modifier la valeur du volume sonnore.
        pygame.mixer.music.set_pos(self.longueur_son/100*float(valeur))

        self.position_son = (self.longueur_son/100*float(valeur))*1000 - pygame.mixer.music.get_pos()


    def set_volume(self, numero):
        # On met à jour les sliders des autres pages en même temps que
        # de récupérer la valeur du slider de la page active.
        if numero == 1:
            valeur = self.volume_1.value()
            self.volume_2.setValue(valeur)
            self.volume_3.setValue(valeur)
            self.volume_4.setValue(valeur)
            self.volume_5.setValue(valeur)
        elif numero == 2:
            valeur = self.volume_2.value()
            self.volume_1.setValue(valeur)
            self.volume_3.setValue(valeur)
            self.volume_4.setValue(valeur)
            self.volume_5.setValue(valeur)
        elif numero == 3:
            valeur = self.volume_3.value()
            self.volume_2.setValue(valeur)
            self.volume_1.setValue(valeur)
            self.volume_4.setValue(valeur)
            self.volume_5.setValue(valeur)
        elif numero == 4:
            valeur = self.volume_4.value()
            self.volume_2.setValue(valeur)
            self.volume_1.setValue(valeur)
            self.volume_3.setValue(valeur)
            self.volume_5.setValue(valeur)
        else:
            valeur = self.volume_5.value()
            self.volume_2.setValue(valeur)
            self.volume_1.setValue(valeur)
            self.volume_3.setValue(valeur)
            self.volume_4.setValue(valeur)
        # Et on va aussi venir modifier la valeur du volume sonnore.
        pygame.mixer.music.set_volume(float(valeur) / 100.0)

    def affichage_top_musiques_stream(self):
        ##
        ## ATTENTION ICI
        ## L'AFFICHAGE DES STREAMS, DU TITRE ET DU NOM DE L ARTISTE PEUVENT DEBORDER
        ## FAIRE DES TESTS POUR NE PAS DEBORDER !!!!
        ##
        top_musics = self._music_controller.get_top_musics()
        # Tout d'abord on initialise les variables pour ne pas avoir de problème
        self.musique_1 = None
        self.musique_2 = None
        self.musique_3 = None
        # Première musique en terme de stream :
        if len(top_musics) >= 1:
            self.musique_1 = top_musics[0]
            chemin_cover_image = self.musique_1['chemin_cover_image']
            self.pushButton_8.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_8.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.musique_1['titre'] + "\n" + self.musique_1['artiste']
            self.label_top_musique1_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_musique1_1.setFont(font)
            streams = str(self.musique_1['stream']) + " streams"
            self.label_top_musique1_2.setText(streams)
        # Deuxième
        if len(top_musics) >= 2:
            self.musique_2 = top_musics[1]
            chemin_cover_image = self.musique_2['chemin_cover_image']
            self.pushButton_9.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_9.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.musique_2['titre'] + "\n" + self.musique_2['artiste']
            self.label_top_musique2_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_musique2_1.setFont(font)
            streams = str(self.musique_2['stream']) + " streams"
            self.label_top_musique2_2.setText(streams)
        # Troisième
        if len(top_musics) >= 3:
            self.musique_3 = top_musics[2]
            chemin_cover_image = self.musique_3['chemin_cover_image']
            self.pushButton_10.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_10.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.musique_3['titre'] + "\n" + self.musique_3['artiste']
            self.label_top_musique3_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_musique3_1.setFont(font)
            streams = str(self.musique_3['stream']) + " streams"
            self.label_top_musique3_2.setText(streams)

    def affichage_top_albums_stream(self):
        ##
        ## ATTENTION ICI
        ## L'AFFICHAGE DES STREAMS, DU TITRE ET DU NOM DE L ARTISTE PEUVENT DEBORDER
        ## FAIRE DES TESTS POUR NE PAS DEBORDER !!!!
        ##
        top_albums = self._playlist_controller.get_top_albums()
        # Tout d'abord on initialise les variables pour ne pas avoir de problème
        self.album_1 = None
        self.album_2 = None
        self.album_3 = None
        # Première musique en terme de stream :
        if len(top_albums) >= 1:
            self.album_1 = top_albums[0]
            chemin_cover_image = self.album_1['chemin_image']
            print(self.album_1['nom'], self.album_1['chemin_image'])
            self.pushButton_4.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_4.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.album_1['nom'] + "\n" + self.album_1['artiste']
            self.label_top_playlist1_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_playlist1_1.setFont(font)
            streams = str(self.album_1['nombre_ecoutes']) + " streams"
            self.label_top_playlist1_2.setText(streams)
        if len(top_albums) >= 2:
            self.album_2 = top_albums[1]
            chemin_cover_image = self.album_2['chemin_image']
            print(self.album_2['nom'], self.album_2['chemin_image'])
            self.pushButton_5.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_5.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.album_2['nom'] + "\n" + self.album_2['artiste']
            self.label_top_playlist2_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_playlist2_1.setFont(font)
            streams = str(self.album_2['nombre_ecoutes']) + " streams"
            self.label_top_playlist2_2.setText(streams)
        if len(top_albums) >= 3:
            self.album_3 = top_albums[2]
            chemin_cover_image = self.album_3['chemin_image']
            print(self.album_3['nom'], self.album_3['chemin_image'])
            self.pushButton_13.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_cover_image)))
            # Faire attention, si on change la taille du boutton en haut de changer la taille de l'icon ici (idem pour les autres)
            self.pushButton_13.setIconSize(QSize(80, 80))
            # On met le texte :
            texte = self.album_3['nom'] + "\n" + self.album_3['artiste']
            self.label_top_playlist3_1.setText(texte)
            font = QtGui.QFont()
            font.setBold(True)
            self.label_top_playlist3_1.setFont(font)
            streams = str(self.album_3['nombre_ecoutes']) + " streams"
            self.label_top_playlist3_2.setText(streams)
        print(self._playlist_controller.liste_playlists)

    def lecture_musique_top(self, numero_top):
        if numero_top == 1:
            musique = self.musique_1
            # Et on fixe l'id
            self.id = musique['id']
        elif numero_top == 2:
            musique = self.musique_2
            # Et on fixe l'id
            self.id = musique['id']
        else:
            musique = self.musique_3
            # Et on fixe l'id
            self.id = musique['id']
        if musique == None:
            return
        self.lire_musique(musique)

    def lire_musique(self, musique):

        ##ATTENTION, pygame.mixer.music.get_pos() est nulle ...
        '''This gets the number of milliseconds that the music has been playing for. The returned time only represents how long the music has been playing; it does not take into account any starting position offsets.'''
        #Je note ici le problème :
        #Tout d'abord, le pygame.mixer.music.set_pos() permet de définir l'endroit de la musique
        #où la musique sera (en secondes)
        #alors que le get_pos() retourne en millisecondes
        #et surtout, le get_pos() retourne seulement le temps que la musique a mis à être écoutée
        #donc avec un set_pos() ça ne prend pas en compte, il faut donc stocker les valeurs...




        playlist = list()
        playlist.append(r"" + musique['chemin_musique'])

        pygame.mixer.music.load(playlist.pop())  # On récupère la musique
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # On met en place l'évènement lorsque la musique se termine
        pygame.mixer.music.play()  # et on fait play

        ##
        self._temp_controller.lecture_musique(musique)
        # On actualise l'id :
        self.id = musique['id']
        # On actualise le nombre de streams
        self.affichage_top_musiques_stream()
        # On actualise le nombre de streams des albums
        self.affichage_top_albums_stream()
        # On actualise l'affichage de la musique en cours :
        self.affichage_cover_titre_artiste(musique)
        # on oublie pas de démarrer la musique si elle est en pause
        if self.etat_musique != "Play":
            self.toogle_etat_musique()
        # Et on reset le coeur
        self.test_like()

        #On utilise un package pour connaître la longueur du son
        #le mixer.music ne l'offre pas
        #une autre possibilité était d'utiliser mixer.Sound mais ça charge le son...
        audio = mutagen.File(r"" + musique['chemin_musique'])
        self.longueur_son = audio.info.length

        #variable qui va servir d'avoir une vraie pos (contrairement au get_pos())
        self.position_son = 0

        #Tant que la musique est lue :
        #on met à jour les sliders
        #et on crée un event quand la musique se termine
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:  # Si la musique se finie
                    # On démarre la musique suivante, qui appartient à l'album
                    return self.changer_musique(1, self.id)
            if (pygame.mixer.music.get_pos() + int(self.position_son)) % 2000 == 0:
                if self.page_active == 0:
                    self.temps_1.setValue(((pygame.mixer.music.get_pos() + int(self.position_son)) / self.longueur_son * 1 / 10) + 1)
                elif self.page_active == 1:
                    self.temps_2.setValue(pygame.mixer.music.get_pos() / self.longueur_son * 1 / 10)
                elif self.page_active == 2:
                    self.temps_3.setValue(pygame.mixer.music.get_pos() / self.longueur_son * 1 / 10)
                elif self.page_active == 5:
                    self.temps_4.setValue(pygame.mixer.music.get_pos() / self.longueur_son * 1 / 10)
                elif self.page_active == 6:
                    self.temps_5.setValue(pygame.mixer.music.get_pos() / self.longueur_son * 1 / 10)

    def changer_musique(self, test, id):
        if id != None:
            musique = self._temp_controller.change_musique(test, id)
            self.lire_musique(musique)

    def affichage_albums(self, numero):
        if numero == 1:
            artiste = self.album_1['artiste']
        elif numero == 2:
            artiste = self.album_2['artiste']
        else:
            artiste = self.album_3['artiste']
        self.affichage_albums_artiste(artiste)

    def affichage_albums_artiste(self, artiste):
        # Ici, il faut recacher tous les boutons qui ont possiblement été décachés juste avant :
        self.boutton_album_cache()
        # On récupère tous les albums de l'artiste en question
        albums = self._playlist_controller.get_albums(artiste)
        # On actualise les écoutes de chaque album
        for album in albums:
            self._playlist_controller.actualisation_ecoutes(album)
        nombre_albums = len(albums)
        if nombre_albums == 1 or nombre_albums == 0:
            self.nom_artiste.setText(artiste + " : album")
        else:
            self.nom_artiste.setText(artiste + " : albums")

        for i in range(nombre_albums):
            chemin_image = albums[i].chemin_image
            if i == 0:
                self.pushButton_album1.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album1.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album1.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album1.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album1.setStyleSheet("text-align:left")
                self.pushButton_album1.clicked.connect(lambda: self.page_album(albums[0]))
                self.pushButton_album1.show()
            elif i == 1:
                self.pushButton_album2.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album2.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album2.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album2.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album2.setStyleSheet("text-align:left")
                self.pushButton_album2.clicked.connect(lambda: self.page_album(albums[1]))
                self.pushButton_album2.show()
            elif i == 2:
                self.pushButton_album3.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album3.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album3.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album3.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album3.setStyleSheet("text-align:left")
                self.pushButton_album3.clicked.connect(lambda: self.page_album(albums[2]))
                self.pushButton_album3.show()
            elif i == 3:
                self.pushButton_album4.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album4.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album4.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album4.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album4.setStyleSheet("text-align:left")
                self.pushButton_album4.clicked.connect(lambda: self.page_album(albums[3]))
                self.pushButton_album4.show()
            elif i == 4:
                self.pushButton_album5.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album5.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album5.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album5.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album5.setStyleSheet("text-align:left")
                self.pushButton_album5.clicked.connect(lambda: self.page_album(albums[4]))
                self.pushButton_album5.show()
            elif i == 5:
                self.pushButton_album6.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album6.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album6.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album6.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album6.setStyleSheet("text-align:left")
                self.pushButton_album6.clicked.connect(lambda: self.page_album(albums[5]))
                self.pushButton_album6.show()
            elif i == 6:
                self.pushButton_album7.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album7.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album7.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album7.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album7.setStyleSheet("text-align:left")
                self.pushButton_album7.clicked.connect(lambda: self.page_album(albums[6]))
                self.pushButton_album7.show()
            elif i == 7:
                self.pushButton_album8.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album8.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album8.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album8.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album8.setStyleSheet("text-align:left")
                self.pushButton_album8.clicked.connect(lambda: self.page_album(albums[7]))
                self.pushButton_album8.show()
            elif i == 8:
                self.pushButton_album9.setIcon(QtGui.QIcon(QtGui.QPixmap(r"" + chemin_image)))
                self.pushButton_album9.setIconSize(QSize(80, 80))
                if albums[i].nombre_ecoutes == 1 or albums[i].nombre_ecoutes == 0:
                    self.pushButton_album9.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoute !")
                else:
                    self.pushButton_album9.setText(albums[i].nom + "\n" + str(albums[i].nombre_ecoutes) + " écoutes !")
                # On applique un StyleSheet pour fixer l'icone à gauche
                self.pushButton_album9.setStyleSheet("text-align:left")
                self.pushButton_album9.clicked.connect(lambda: self.page_album(albums[8]))
                self.pushButton_album9.show()

    def like(self):
        if self.couleur == "noir":
            playlist = self._temp_controller.add_music_like()
            self.set_heart_red()
        else:
            playlist = self._temp_controller.delete_music_like()
            self.set_heart_black()
        # On actualise les artistes préférés :
        self.affichage_artistes_preferes()

    # Fonction à intégrer dans le future fonction de lecture
    def test_like(self):
        test = self._temp_controller.islike()
        if test:
            self.set_heart_red()
        else:
            self.set_heart_black()

    # Affichage des artistes préférés
    def affichage_artistes_preferes(self):
        playlist = self._temp_controller.get_playlist_like()
        # On reset les artistes préférés
        self.pushButton_3.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        # On actualise l'artiste préféré de l'utilisateur
        if len(playlist.top_artistes) >= 1:
            self.pushButton_3.setText(playlist.top_artistes[0]['nom'])
        if len(playlist.top_artistes) >= 2:
            self.pushButton_6.setText(playlist.top_artistes[1]['nom'])
        if len(playlist.top_artistes) >= 3:
            self.pushButton_7.setText(playlist.top_artistes[2]['nom'])

    # Pour modifier le mot de passe de l'utilisateur
    def modification_de_compte(self):
        if(self._member_controller.modification_de_compte(
            [self.lineEdit_mot_de_passe_3.text(), self.lineEdit_mot_de_passe_4.text(),
             self.lineEdit_mot_de_passe_5.text()], self._temp_controller.retour_user(), self.Dialog) == 1):
            self.page(2)

    # Pour supprimer le compte
    def suppression_de_compte(self):
        self._member_controller.suppression_de_compte(self._temp_controller.retour_user())
        self.page(3)

    # On initiale le pygame mixer ici
    def initialisation_pygame_mixer(self):
        # initialize pygame.mixer
        pygame.mixer.init(frequency=44100, size=-16, channels=0, buffer=2 ** 12)
        self.channel = pygame.mixer.Channel(0)