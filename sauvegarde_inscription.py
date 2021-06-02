from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5 import QtCore, QtGui, QtWidgets
from vue.member_vue import MemberVue

from vue.common import Common
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon, QPixmap
import smtplib, ssl


class Ui_Dialog(MemberVue):
    def __init__(self, member_controller):
        super().__init__(member_controller)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 400)
        #setup de la page d'inscription
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
        self.comboBox.setItemText(2, _translate("Dialog", "Mongolie"))
        self.comboBox.setItemText(3, _translate("Dialog", "Congo"))
        self.comboBox.setItemText(4, _translate("Dialog", "République Démocratique du Congo"))
        self.comboBox.setItemText(5, _translate("Dialog", "Kergistkan"))
        self.comboBox.setItemText(6, _translate("Dialog", "Chine"))
        self.comboBox.setItemText(7, _translate("Dialog", "Australie"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Sexe"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Femme"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Homme"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Autre"))
        self.label.setText(_translate("Dialog", "Date de naissance"))
    #creation de compte
    def creation_du_compte(self, Dialog):
        #verif si les cgu sont acceptees
        if not self.checkBox.isChecked():
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Veuillez accepter les conditions d\'utilisation pour utiliser nos services.')
            return 0
        #si adresse mail invalide
        if not test_adresse_mail(self.lineEdit.text(), Dialog):
            return 0
        email = self.lineEdit.text()
        #pareil pour le mdp
        if not test_mot_de_passe(self.lineEdit_2.text(), self.lineEdit_3.text(), Dialog):
            return 0
        pseudo = self.lineEdit_4.text()
        mot_de_passe = self.lineEdit.text()
        #si l'utilisateur n'a pas indique son sexe
        if self.comboBox_2.currentText() == "Sexe":
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Veuillez entrer un sexe')
            return 0
        sexe = self.comboBox_2.currentText()
        # si pas indique son pays
        if self.comboBox.currentText() == "Pays":
            error_dialog = QtWidgets.QErrorMessage(Dialog)
            error_dialog.showMessage('Veuillez entrer votre Pays')
            return 0
        pays = self.comboBox.currentText()
        member = self.add_member([email, pseudo, mot_de_passe, sexe, pays])
        self.show_member(member)
        self.show_members()


#verification de l'adresse mail, format valide...
def test_adresse_mail(adresse, Dialog):
    if "@" not in adresse:
        error_dialog = QtWidgets.QErrorMessage(Dialog)
        error_dialog.showMessage('Votre adresse mail n\'est pas valide')
        return False
    indice = adresse.index('@')
    analyse = adresse[indice:]
    if "." not in analyse:
        error_dialog = QtWidgets.QErrorMessage(Dialog)
        error_dialog.showMessage('Votre adresse mail n\'est pas valide')
        return False
    return True

def test_mot_de_passe(mot_de_passe1, mot_de_passe2,Dialog):
    #On ne veut pas d'espace dans le mot de passe
    if " " in mot_de_passe1:
        error_dialog = QtWidgets.QErrorMessage(Dialog)
        error_dialog.showMessage('Votre mot de passe ne peut pas avoir d\'espace... !')
        return False
    #Tout d'abord, si le mot de passe à une longueur inférieure à 6 (pour une sécurité/optionnel)
    if len(mot_de_passe1) < 6:
        error_dialog = QtWidgets.QErrorMessage(Dialog)
        error_dialog.showMessage('Votre mot de passe doit au minimum contenir 6 caractères !')
        return False
    #Puis si les mots de passe sont différents
    if mot_de_passe2 != mot_de_passe1:
        error_dialog = QtWidgets.QErrorMessage(Dialog)
        error_dialog.showMessage('Vos mots de passe ne correspondent pas.')
        return False
    return True





























































































































#https: // www.quennec.fr / trucs - astuces / langages / python / python - envoyer - un - mail - tout - simplement
#https://datascientest.com/comment-envoyer-un-e-mail-avec-python
'''smtp_address = 'smtp.gmail.com'
smtp_port = 587

email_address = 'spotython@gmail.com'
email_password = 'ceciestuntest'

#email_receiver = self.lineEdit.text()
email_receiver = 'pajot.matt@gmail.com'

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    # connexion au compte
    server.login(email_address, email_password)
    # envoi du mail
    server.sendmail(email_address, email_receiver, 'le contenu de l\'e-mail')'''

'''import smtplib


msg = MIMEMultipart()
msg['From'] = 'spotython@gmail.com'
msg['To'] = 'spotython@gmail.com'
msg['Subject'] = 'Le sujet de mon mail'
message = 'Bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('spotython@gmail.com', 'ceciestuntest')
mailserver.sendmail('spotython@gmail.com', 'spotython@gmail.com', msg.as_string())
mailserver.quit()'''