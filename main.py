from vue.accueil_vue import Ui_Accueil
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from controller.music_controller import MusicController


#TEMPORAIREMENT
from vue.lecture_vue import Ui_Lecture

#TEMPORAIREMENT VRAIMENT
from vue.temp import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == '__main__':
    database_engine_1 = DatabaseEngine(url='sqlite:///compte.db')
    _member_controller = MemberController(database_engine_1)
    database_engine_2 = DatabaseEngine(url='sqlite:///musique.db')
    _music_controller = MusicController(database_engine_2)


    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(r"support\Interface\icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(_member_controller, _music_controller)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    #La table de données liée au compte utilisateur
    '''database_engine = DatabaseEngine(url='sqlite:///compte.db')
    database_engine.create_database()

    _member_controller = MemberController(database_engine)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Accueil(_member_controller)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())'''



'''app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    Dialog.setStyleSheet("background-color: rgb(200,210,250)")
    ui = Ui_Lecture()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())'''





