from vue.accueil_vue import Ui_Accueil
from model.database import DatabaseEngine


#TEMPORAIREMENT
from vue.lecture_vue import Ui_Lecture
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
    '''
    #La table de données liée au compte utilisateur
    database_engine = DatabaseEngine(url='sqlite:///compte.db')
    database_engine.create_database()
    ui = Ui_Accueil(database_engine)
    ui.setupUi()'''
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setStyleSheet("background-color: rgb(200,210,250)")
    ui = Ui_Lecture()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


