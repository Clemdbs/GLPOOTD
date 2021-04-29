from PyQt5 import QtCore, QtWidgets
from vue.member_vue import MemberVue

class Ui_Dialog(MemberVue):
    def __init__(self, member_controller):
        super().__init__(member_controller)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 400)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 240, 261, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 270, 261, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 100, 161, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 40, 161, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 210, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 180, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(20, 150, 161, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 130, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        #Ici, on va faire en sorte que le programme exécute une fonction s'il clique sur "ok"
        self.buttonBox.accepted.connect(lambda: self.creation_du_compte(Dialog))


        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "J\'accepte les conditions d\'utilisation"))
        self.checkBox_2.setText(_translate("Dialog", "Je m\'abonne à la newsletter"))
        self.lineEdit.setText(_translate("Dialog", "Adresse mail"))
        self.lineEdit_2.setText(_translate("Dialog", "Mot de passe"))
        self.lineEdit_3.setText(_translate("Dialog", "Confirmation de mot de passe"))
        self.lineEdit_4.setText(_translate("Dialog", "Pseudo"))
        self.comboBox.setItemText(0, _translate("Dialog", "Pays"))
        self.comboBox.setItemText(1, _translate("Dialog", "France"))
        self.comboBox.setItemText(2, _translate("Dialog", "Russie"))
        self.comboBox.setItemText(3, _translate("Dialog", "Congo"))
        self.comboBox.setItemText(4, _translate("Dialog", "Allemagne"))
        self.comboBox.setItemText(5, _translate("Dialog", "Italie"))
        self.comboBox.setItemText(6, _translate("Dialog", "Chine"))
        self.comboBox.setItemText(7, _translate("Dialog", "Australie"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Sexe"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Femme"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Homme"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Autre"))
        self.label.setText(_translate("Dialog", "Date de naissance"))

    def creation_du_compte(self, Dialog):
        #Si le bouton n'est pas accepté
        if not self.checkBox.isChecked():
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Veuillez accepter les conditions d\'utilisation pour utiliser nos services.')
            return 0
        # Puis si les mots de passe sont différents
        if self.lineEdit_2.text() != self.lineEdit_3.text():
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Vos mots de passe ne correspondent pas.')

        email = self.lineEdit.text()
        pseudo = self.lineEdit_4.text()
        mot_de_passe = self.lineEdit.text()
        sexe = self.comboBox_2.currentText()
        pays = self.comboBox.currentText()


        member = self.add_member([email, pseudo, mot_de_passe, sexe, pays])
        if isinstance(member, str):
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage(member)

        self.show_member(member)
        ####
        #FAIRE UN TEST POUR PAS DEUX COMPTES IDENTIQUES CAR SÛREMENT PAS GERE ICI
        ####
        self.show_members()