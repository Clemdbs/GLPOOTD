from PyQt5 import QtCore, QtGui, QtWidgets
from vue.inscription_vue import Ui_Dialog
from controller.member_controller import MemberController
from vue.member_vue import MemberVue
from vue.lecture_vue import Ui_Lecture
import sys


class Ui_Accueil(MemberVue):
    def __init__(self, member_controller):
        super().__init__(member_controller)
        self._member_controller = member_controller

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 401)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Dialog.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(210, 10, 101, 20))
        #Changer le style de police :
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 350, 91, 22))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 151, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 180, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 140, 113, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Accueil", "Dialog"))
        self.label.setText(_translate("Accueil", "Spotython"))
        self.pushButton.setText(_translate("Accueil", "Pas de compte ?"))
        self.label_2.setText(_translate("Accueil", "Adresse mail :"))
        self.label_3.setText(_translate("Accueil", "Mot de passe :"))
        self.pushButton_2.setText(_translate("Accueil", "Connection"))

        self.pushButton.clicked.connect(lambda: self.inscription())
        self.pushButton_2.clicked.connect(lambda: self.connection())

    def inscription(self):
        ui = Ui_Dialog(self._member_controller)
        Dialog = QtWidgets.QDialog()
        ui.setupUi(Dialog)
        Dialog.show()

    def connection(self):
        #Là où on affichera la page avec les différents onglets
        self.show_members()

        email = self.lineEdit.text()
        mot_de_passe = self.lineEdit_2.text()
        member = self._member_controller.search_member(email)

        print(member)

        if member == None: #si le compte n'existe pas :
            print("Compte non existant")    #on affiche que le compte n'existe pas
        else:  # si le compte existe, on affiche le compte lié au mdp
            print(member['mot_de_passe'])
            if(self._member_controller.connection(email, mot_de_passe)):
                Dialog = QtWidgets.QDialog()
                Dialog.setStyleSheet("background-color: rgb(200,210,250)")
                ui = Ui_Lecture()
                ui.setupUi(Dialog)
                Dialog.show()
            else:
                print("non")