from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import sys


class Ui_Lecture(object):
    def __init__(self):
        pygame.init()

        self.song = pygame.mixer.Sound(r"support\Musique\Eminem\Lose_Yourself\Lose_Yourself.ogg")
        self.song.play()
        self.song.set_volume(0.4)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 401)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(470, 50, 50, 64))
        self.dial.setObjectName("dial")
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(40)

        self.dial.valueChanged.connect(self.change_volume)
        self.label_titre = QtWidgets.QLabel(Dialog)
        self.label_titre.setGeometry(QtCore.QRect(200, 70, 231, 31))
        self.label_titre.setText("")
        self.label_titre.setObjectName("label_titre")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(492, 105, 21, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 151, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(r"support\Musique\Eminem\Lose_Yourself\Lose_Yourself.jpg"))
        self.titre = "Lose Yourself"
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 51, 22))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_gauche.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 170, 51, 22))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"support\Interface\flèche_droite.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_music = QtWidgets.QPushButton(Dialog)
        self.pushButton_music.setGeometry(QtCore.QRect(85, 170, 20, 22))
        self.pushButton_music.setText("")

        #Pour tester si la musique est entrain de jouer ou pas
        self.music = "play"
        #Icone pause :
        self.icon_pause = QtGui.QIcon()
        self.icon_pause.addPixmap(QtGui.QPixmap(r"support\Interface\pause.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #Icone play :
        self.icon_play = QtGui.QIcon()
        self.icon_play.addPixmap(QtGui.QPixmap(r"support\Interface\play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_music.setIcon(self.icon_pause)
        self.pushButton_music.setObjectName("pushButton_pause")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 200, 31, 22))
        self.pushButton_3.setText("")
        self.icon_coeur_vide = QtGui.QIcon()
        self.icon_coeur_vide.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_vide.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_coeur_plein = QtGui.QIcon()
        self.icon_coeur_plein.addPixmap(QtGui.QPixmap(r"support\Interface\coeur_plein.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.couleur = "noir"


        self.pushButton_3.setIcon(self.icon_coeur_vide)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.toogle_heart)
        #Ligne pour enlever les bordures. Voir le commentaire du dessous.
        self.pushButton_3.setStyleSheet("border-style:outset")

        #Ici, on ajoute la fonction quand on clique sur le bouton pause
        self.pushButton_music.clicked.connect(self.toogle_music)


        icon_plus = QtGui.QIcon()
        icon_plus.addPixmap(QtGui.QPixmap(r"support\Interface\plus.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_plus_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_plus_1.setGeometry(QtCore.QRect(175, 105, 20, 20))
        self.pushButton_plus_1.setText("")
        self.pushButton_plus_1.setIcon(icon_plus)
        self.pushButton_plus_1.setFlat(True)
        self.pushButton_plus_1.setFocusPolicy(False)
        #Cette ligne du dessous est juste pas bonne pour appliquer celles du dessus.
        #Etrange mais le CSS ne fonctionne pas parfaitement j'ai l'impression.
        #En fait, elle supprime le CSS et du coup niveau rendu, bah là ça va
        self.pushButton_plus_1.setStyleSheet("border-style:outset")
        self.pushButton_plus_1.clicked.connect(self.ok)

        #Titre de la musique
        self.label_titre.setText(self.titre)
        self.label_titre.setFont(font)
        #Nom de l'artiste dans un bouton avec bordures cachees
        self.nom_artiste = QtWidgets.QPushButton(Dialog)
        self.nom_artiste.setGeometry(QtCore.QRect(200, 100, 231, 31))
        self.nom_artiste.setText("Eminem")
        self.nom_artiste.setStyleSheet("QPushButton { text-align: left; }")
        self.nom_artiste.setFlat(True)
        self.nom_artiste.setFocusPolicy(False)
        #mais là je peux pas utiliser le bug car si je n'ai plus le css, le texte ne peut pas être alligné à gauche...

        #Volume sonore
        self.label_2.setText(str(self.dial.value()))

        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok(self):
        print("ok")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def toogle_heart(self):
        if self.couleur == "rouge":
            self.couleur = "noir"
            self.pushButton_3.setIcon(self.icon_coeur_vide)
        else:
            self.couleur = "rouge"
            self.pushButton_3.setIcon(self.icon_coeur_plein)

    def toogle_music(self):
        if self.music == "play":
            self.music = "stop"
            self.pushButton_music.setIcon(self.icon_play)
            pygame.mixer.pause()
        else:
            self.music = "play"
            self.pushButton_music.setIcon(self.icon_pause)
            pygame.mixer.unpause()

    def change_volume(self):
        if self.dial.value() > 100:
            self.dial.setValue(100)
        if self.dial.value() < 0:
            self.dial.setValue(0)
        self.label_2.setText(str(self.dial.value()))
        self.song.set_volume(float(self.dial.value())/100.0)