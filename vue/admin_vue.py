from PyQt5 import QtCore, QtGui, QtWidgets
from controller.music_controller import MusicController
from vue.music_vue import MusicVue
import sys

class Ajout_musique(MusicVue):
    def __init__(self, member_controller):
        super().__init__(member_controller)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(354, 10, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 201, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 150, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 200, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 201, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 201, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 201, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 201, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 300, 201, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 380, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 201, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 350, 201, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 400, 201, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 470, 121, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(400, 470, 121, 22))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Dialog)
        self.pushButton3.setGeometry(QtCore.QRect(600, 470, 121, 22))
        self.pushButton3.setObjectName("pushButton3")

        self.retranslateUi(Dialog)
        # Ici, on va faire en sorte que le programme exécute une fonction s'il clique sur "Ajouter"
        self.pushButton.clicked.connect(lambda: self.creation_du_compte(Dialog))

        self.pushButton2.clicked.connect(lambda: self.show())
        self.pushButton3.clicked.connect(lambda: self.ask())

        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Panneau de contrôle pour administrateur"))
        self.label_2.setText(_translate("Dialog", "Titre :"))
        self.label_3.setText(_translate("Dialog", "Artiste :"))
        self.label_4.setText(_translate("Dialog", "Album :"))
        self.label_5.setText(_translate("Dialog", "Type :"))
        self.label_6.setText(_translate("Dialog", "Chemin image cover :"))
        self.label_7.setText(_translate("Dialog", "Chemin musique :"))
        self.pushButton.setText(_translate("Dialog", "Valider"))
        self.pushButton2.setText(_translate("Dialog", "Afficher la bdd"))

    def creation_du_compte(self, Dialog):
        titre = self.lineEdit.text()
        artiste = self.lineEdit_2.text()
        album = self.lineEdit_3.text()
        type = self.lineEdit_4.text()
        chemin_musique = self.lineEdit_5.text()
        chemin_cover_image = self.lineEdit_6.text()

        music = self.add_music([titre, artiste, album, type, chemin_musique, chemin_cover_image])
        if isinstance(music, str):
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage(music)

        self.show_music(music)
        ####
        #FAIRE UN TEST POUR PAS DEUX COMPTES IDENTIQUES CAR SÛREMENT PAS GERE ICI
        ####
        self.show_musics()

    def show(self):
        self.show_musics()
    def ask(self):
        self.search_music()
