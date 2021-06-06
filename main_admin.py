from PyQt5 import QtCore, QtGui, QtWidgets
from vue.admin_vue import Pannel_admin
from model.database import DatabaseEngine
from controller.music_controller import MusicController
from controller.music_like_controller import Music_LikeController
from controller.member_controller import MemberController
import sys


if __name__ == "__main__":
    # La table de données liée au compte utilisateur
    database_engine = DatabaseEngine(url='sqlite:///musique.db')
    database_engine.create_database()

    _music_controller = MusicController(database_engine)
    _music_like_controller = Music_LikeController(database_engine)
    _member_controller = MemberController(database_engine)


    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Pannel_admin(_music_controller, _music_like_controller, _member_controller)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())