from PyQt5 import QtCore, QtGui, QtWidgets
from vue.music_vue import MusicVue
from vue.member_vue import MemberVue


class Pannel_admin():
    def __init__(self, music_controller, music_like_controller, member_controller):
        self._music_controller = music_controller
        self._music_like_controller = music_like_controller
        self._member_controller = member_controller
        self._music_vue = MusicVue(self._music_controller)
        self._member_vue = MemberVue(self._member_controller)
    def setupUi(self, Dialog):
        #affichage et boutons de la page musique
        Dialog.setObjectName("Dialog")
        Dialog.resize(1080, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)

        ###
        # PAGE 1 - AJOUT DE MUSIQUE(S)
        ###

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget.setObjectName("widget")
        self.pushButton_valider_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_valider_2.setGeometry(QtCore.QRect(40, 555, 201, 22))
        self.pushButton_valider_2.setObjectName("pushButton_valider_2")
        self.label_album_1 = QtWidgets.QLabel(self.widget)
        self.label_album_1.setGeometry(QtCore.QRect(40, 310, 201, 21))
        self.label_album_1.setObjectName("label_album_1")
        self.label_chemin_musique = QtWidgets.QLabel(self.widget)
        self.label_chemin_musique.setGeometry(QtCore.QRect(40, 410, 201, 21))
        self.label_chemin_musique.setObjectName("label_chemin_musique")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setGeometry(QtCore.QRect(40, 285, 201, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_artiste_1 = QtWidgets.QLabel(self.widget)
        self.label_artiste_1.setGeometry(QtCore.QRect(40, 260, 201, 21))
        self.label_artiste_1.setObjectName("label_artiste_1")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setGeometry(QtCore.QRect(40, 235, 201, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setGeometry(QtCore.QRect(40, 385, 201, 21))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_chemin_image_cover = QtWidgets.QLabel(self.widget)
        self.label_chemin_image_cover.setGeometry(QtCore.QRect(40, 460, 201, 21))
        self.label_chemin_image_cover.setObjectName("label_chemin_image_cover")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setGeometry(QtCore.QRect(40, 435, 201, 21))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_titre_1 = QtWidgets.QLabel(self.widget)
        self.label_titre_1.setGeometry(QtCore.QRect(40, 200, 201, 31))
        self.label_titre_1.setObjectName("label_titre_1")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setGeometry(QtCore.QRect(40, 335, 201, 21))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_type = QtWidgets.QLabel(self.widget)
        self.label_type.setGeometry(QtCore.QRect(40, 360, 201, 21))
        self.label_type.setObjectName("label_type")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setGeometry(QtCore.QRect(40, 485, 201, 21))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

        self.label_ajouter_toutes_musiques = QtWidgets.QLabel(self.widget)
        self.label_ajouter_toutes_musiques.setGeometry(QtCore.QRect(40, 40, 1071, 121))
        font.setWeight(45)
        self.label_ajouter_toutes_musiques.setFont(font)
        self.label_ajouter_toutes_musiques.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ajouter_toutes_musiques.setObjectName("label_ajouter_toutes_musiques")

        self.pushButton_valider_1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_valider_1.setGeometry(QtCore.QRect(40, 130, 201, 22))
        self.pushButton_valider_1.setObjectName("pushButton_valider_1")

        self.label_ajouter_une_musique = QtWidgets.QLabel(self.widget)
        self.label_ajouter_une_musique.setGeometry(QtCore.QRect(40, 120, 1071, 121))
        self.label_ajouter_une_musique.setFont(font)
        self.label_ajouter_une_musique.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ajouter_une_musique.setObjectName("label_ajouter_une_musique")

        self.tabWidget.addTab(self.tab, "")

        ###
        # PAGE 2 - SUPPRESSION DE MUSIQUE(S)
        ###

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_2 = QtWidgets.QWidget(self.tab_2)
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_valider_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_valider_4.setGeometry(QtCore.QRect(40, 405, 201, 22))
        self.pushButton_valider_4.setObjectName("pushButton_valider_4")
        self.label_album_2 = QtWidgets.QLabel(self.widget_2)
        self.label_album_2.setGeometry(QtCore.QRect(40, 310, 201, 21))
        self.label_album_2.setObjectName("label_album_2")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(40, 285, 201, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_artiste_2 = QtWidgets.QLabel(self.widget_2)
        self.label_artiste_2.setGeometry(QtCore.QRect(40, 260, 201, 21))
        self.label_artiste_2.setObjectName("label_artiste_2")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(40, 235, 201, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_titre_2 = QtWidgets.QLabel(self.widget_2)
        self.label_titre_2.setGeometry(QtCore.QRect(40, 200, 201, 31))
        self.label_titre_2.setObjectName("label_titre_2")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(40, 335, 201, 21))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_26 = QtWidgets.QLabel(self.widget_2)
        self.label_26.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setObjectName("label_26")

        self.label_supprimer_toutes_musiques = QtWidgets.QLabel(self.widget_2)
        self.label_supprimer_toutes_musiques.setGeometry(QtCore.QRect(40, 40, 1071, 121))
        font.setWeight(45)
        self.label_supprimer_toutes_musiques.setFont(font)
        self.label_supprimer_toutes_musiques.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_supprimer_toutes_musiques.setObjectName("label_supprimer_toutes_musiques")

        self.pushButton_valider_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_valider_3.setGeometry(QtCore.QRect(40, 130, 201, 22))
        self.pushButton_valider_3.setObjectName("pushButton_valider_3")

        self.label_supprimer_une_musique = QtWidgets.QLabel(self.widget_2)
        self.label_supprimer_une_musique.setGeometry(QtCore.QRect(40, 120, 1071, 121))
        self.label_supprimer_une_musique.setFont(font)
        self.label_supprimer_une_musique.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_supprimer_une_musique.setObjectName("label_supprimer_une_musique")

        self.tabWidget.addTab(self.tab_2, "")

        ###
        # PAGE 3 - VISUELS POUR MUSIQUES
        ###

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.label_Visuel_1 = QtWidgets.QLabel(self.tab_6)
        self.label_Visuel_1.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Visuel_1.setFont(font)
        self.label_Visuel_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Visuel_1.setObjectName("label_Visuel_1")


        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 100, 181, 22))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 180, 181, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_6, "")

        ###
        # PAGE 4 - SUPPRESSION DE MEMBRE(S)
        ###

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget_4 = QtWidgets.QWidget(self.tab_4)
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 1081, 651))
        self.widget_4.setObjectName("widget_2")
        self.pushButton_valider_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_valider_6.setGeometry(QtCore.QRect(40, 405, 201, 22))
        self.pushButton_valider_6.setObjectName("pushButton_valider_6")
        self.lineEdit_mail = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_mail.setGeometry(QtCore.QRect(40, 235, 201, 21))
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.label_adresse_mail = QtWidgets.QLabel(self.widget_4)
        self.label_adresse_mail.setGeometry(QtCore.QRect(40, 200, 201, 31))
        self.label_adresse_mail.setObjectName("label_adresse_mail")
        self.label_suppression_de_membres = QtWidgets.QLabel(self.widget_4)
        self.label_suppression_de_membres.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_suppression_de_membres.setFont(font)
        self.label_suppression_de_membres.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_suppression_de_membres.setObjectName("label_suppression_de_membres")

        self.label_supprimer_tous_les_membres = QtWidgets.QLabel(self.widget_4)
        self.label_supprimer_tous_les_membres.setGeometry(QtCore.QRect(40, 40, 1071, 121))
        font.setWeight(45)
        self.label_supprimer_tous_les_membres.setFont(font)
        self.label_supprimer_tous_les_membres.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_supprimer_tous_les_membres.setObjectName("label_supprimer_tous_les_membres")

        self.pushButton_valider_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_valider_5.setGeometry(QtCore.QRect(40, 130, 201, 22))
        self.pushButton_valider_5.setObjectName("pushButton_valider_5")

        self.label_supprimer_un_membre = QtWidgets.QLabel(self.widget_4)
        self.label_supprimer_un_membre.setGeometry(QtCore.QRect(40, 120, 1071, 121))
        self.label_supprimer_un_membre.setFont(font)
        self.label_supprimer_un_membre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_supprimer_un_membre.setObjectName("label_supprimer_un_membre")

        self.tabWidget.addTab(self.tab_4, "")

        ###
        # PAGE 5 - VISUELS POUR MEMBRES
        ###

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.label_Visuel_2 = QtWidgets.QLabel(self.tab_5)
        self.label_Visuel_2.setGeometry(QtCore.QRect(40, -20, 1071, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_Visuel_2.setFont(font)
        self.label_Visuel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Visuel_2.setObjectName("label_Visuel_2")

        self.pushButton_afficher_la_bdd = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_afficher_la_bdd.setGeometry(QtCore.QRect(30, 100, 181, 22))
        self.pushButton_afficher_la_bdd.setObjectName("pushButton_afficher_la_bdd")
        self.pushButton_chercher_un_membre = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_chercher_un_membre.setGeometry(QtCore.QRect(30, 180, 181, 22))
        self.pushButton_chercher_un_membre.setObjectName("pushButton_chercher_un_membre")
        self.tabWidget.addTab(self.tab_5, "")

        ###
        # CONSTRUCTION DE LA FENÊTRE
        ###

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        # Ici, on connecte les boutons aux fonctions souhaitées
        self.pushButton_valider_1.clicked.connect(lambda: self.ajoutertouteslesmusiques())
        self.pushButton_valider_2.clicked.connect(lambda: self.creation_de_musique(Dialog))

        self.pushButton_valider_3.clicked.connect(lambda: self.supprimer_toutes_les_musiques())
        self.pushButton_valider_4.clicked.connect(lambda: self.supprimer_musique())

        self.pushButton_7.clicked.connect(lambda: self.show_musiques())
        self.pushButton_6.clicked.connect(lambda: self.ask_musiques())

        self.pushButton_valider_5.clicked.connect(lambda: self.supprimer_tous_les_membres())
        self.pushButton_valider_6.clicked.connect(lambda: self.supprimer_membre())

        self.pushButton_afficher_la_bdd.clicked.connect(lambda: self.show_membres())
        self.pushButton_chercher_un_membre.clicked.connect(lambda: self.ask_membres())



        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        # affichage des boutons et option de la page des musiques
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Administrateur"))

        ###
        # PAGE 1 - AJOUT DE MUSIQUE(S)
        ###

        self.label.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Ajouter des musiques"))
        self.label_ajouter_toutes_musiques.setText(_translate("Dialog", "Ajouter toutes les musiques d'un coup"))
        self.pushButton_valider_1.setText(_translate("Dialog", "Valider"))
        self.label_ajouter_une_musique.setText(_translate("Dialog", "Ajouter une musique"))
        self.label_titre_1.setText(_translate("Dialog", "Titre :"))
        self.label_artiste_1.setText(_translate("Dialog", "Artiste :"))
        self.label_album_1.setText(_translate("Dialog", "Album :"))
        self.label_type.setText(_translate("Dialog", "Type :"))
        self.label_chemin_musique.setText(_translate("Dialog", "Chemin musique :"))
        self.label_chemin_image_cover.setText(_translate("Dialog", "Chemin image cover :"))
        self.pushButton_valider_2.setText(_translate("Dialog", "Valider"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Ajouter des musiques"))

        ###
        # PAGE 2 - SUPPRESSION DE MUSIQUE(S)
        ###

        self.label_Visuel_1.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Visuel pour les musiques"))

        self.label_26.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Supprimer des musiques"))
        self.label_supprimer_toutes_musiques.setText(_translate("Dialog", "Supprimer toutes les musiques d'un coup"))
        self.pushButton_valider_3.setText(_translate("Dialog", "Valider"))
        self.label_supprimer_une_musique.setText(_translate("Dialog", "Supprimer une musique"))
        self.label_titre_2.setText(_translate("Dialog", "Titre :"))
        self.label_artiste_2.setText(_translate("Dialog", "Artiste :"))
        self.label_album_2.setText(_translate("Dialog", "Album :"))
        self.pushButton_valider_4.setText(_translate("Dialog", "Valider"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Supprimer des musiques"))

        ###
        # PAGE 3 - VISUELS POUR MUSIQUES
        ###

        self.label_Visuel_1.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Visuel pour les musiques"))
        self.pushButton_6.setText(_translate("Dialog", "Chercher une musique"))
        self.pushButton_7.setText(_translate("Dialog", "Afficher la bdd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Visuels pour musiques"))

        ###
        # PAGE 4 - SUPPRESSION DE MEMBRE(S)
        ###

        self.label_suppression_de_membres.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Supprimer des membres"))
        self.label_supprimer_tous_les_membres.setText(_translate("Dialog", "Supprimer tous les membres d'un coup"))
        self.pushButton_valider_5.setText(_translate("Dialog", "Valider"))
        self.label_supprimer_un_membre.setText(_translate("Dialog", "Supprimer un membre"))
        self.label_adresse_mail.setText(_translate("Dialog", "Adresse mail :"))
        self.pushButton_valider_6.setText(_translate("Dialog", "Valider"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Supprimer des membres"))

        ###
        # PAGE 5 - VISUELS POUR MUSIQUES
        ###

        self.label_Visuel_2.setText(_translate("Dialog", "Panneau de contrôle pour administrateur : Visuel pour les membres"))
        self.pushButton_afficher_la_bdd.setText(_translate("Dialog", "Afficher la bdd"))
        self.pushButton_chercher_un_membre.setText(_translate("Dialog", "Chercher un membre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Visuels pour membres"))

    #creation de la musique / affichage
    def creation_de_musique(self, Dialog):
        titre = self.lineEdit_14.text()
        artiste = self.lineEdit_13.text()
        album = self.lineEdit_17.text()
        type = self.lineEdit_15.text()
        chemin_musique = self.lineEdit_16.text()
        chemin_cover_image = self.lineEdit_18.text()

        music = self._music_vue.add_music([titre, artiste, album, type, chemin_musique, chemin_cover_image])
        if isinstance(music, str):
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage(music)

        self._music_vue.show_music(music)

    def supprimer_musique(self):
        titre = self.lineEdit_20.text()
        artiste = self.lineEdit_19.text()
        album = self.lineEdit_23.text()
        self._music_vue.delete_music(titre, artiste, album)

    def supprimer_toutes_les_musiques(self):
        self._music_controller.reinitialisation_de_la_base_de_donnees()

    def show_musiques(self):
        self._music_vue.show_musics()
    def ask_musiques(self):
        self._music_vue.search_music()

    def show_membres(self):
        self._member_vue.show_members()
    def ask_membres(self):
        self._member_vue.search_member()

    def ajoutertouteslesmusiques(self):
        print(self._music_controller.list_musics())
        self._music_like_controller.reinitialisation_de_la_base_de_donnees()
        musiques = self._music_controller.initialisation_de_la_base_de_donnees()
        for musique in musiques:
            music = self._music_vue.add_music(musique)
            self._music_vue.show_music(music)

    def supprimer_tous_les_membres(self):
        self._member_controller.reinitialisation_de_la_base_de_donnees()

    def supprimer_membre(self):
        mail = self.lineEdit_mail.text()
        self._member_controller.delete_by_email(mail)

