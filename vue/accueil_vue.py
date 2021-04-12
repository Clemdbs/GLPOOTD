from PyQt5 import QtCore, QtGui, QtWidgets
from vue.inscription_vue import Ui_Dialog
from controller.member_controller import MemberController
import sys


class Ui_Accueil(object):
    def __init__(self, database_engine):
        self.data = database_engine
        self.app = QtWidgets.QApplication(sys.argv)
        self.Accueil = QtWidgets.QDialog()
    def setupUi(self):
        self.Accueil.setObjectName("Dialog")
        self.Accueil.resize(541, 401)
        self.Accueil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Accueil.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(self.Accueil)
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
        self.pushButton = QtWidgets.QPushButton(self.Accueil)
        self.pushButton.setGeometry(QtCore.QRect(50, 350, 91, 22))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.Accueil)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Accueil)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 151, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.Accueil)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 180, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.Accueil)
        self.lineEdit.setGeometry(QtCore.QRect(50, 90, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Accueil)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 140, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(self.Accueil)
        QtCore.QMetaObject.connectSlotsByName(self.Accueil)

        self.Accueil.show()
        sys.exit(self.app.exec_())

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Dialog"))
        self.label.setText(_translate("Accueil", "Spotython"))
        self.pushButton.setText(_translate("Accueil", "Pas de compte ?"))
        self.label_2.setText(_translate("Accueil", "Adresse mail :"))
        self.label_3.setText(_translate("Accueil", "Mot de passe :"))
        self.pushButton_2.setText(_translate("Accueil", "Connection"))

        self.pushButton.clicked.connect(lambda: self.inscription())
        self.pushButton_2.clicked.connect(lambda : self.feuille())

    def inscription(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog(MemberController(self.data))
        ui.setupUi(Dialog)
        Dialog.show()

    def feuille(self):
        #Là où on affichera la page avec les différents onglets
        pass