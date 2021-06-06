from model.database import DatabaseEngine
from controller.member_controller import MemberController
from controller.music_controller import MusicController
from controller.music_like_controller import Music_LikeController

from vue.spythonfy import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == '__main__':
    database_engine = DatabaseEngine(url='sqlite:///musique.db')
    database_engine.create_database()
    _member_controller = MemberController(database_engine)
    _music_controller = MusicController(database_engine)
    _music_like_controller = Music_LikeController(database_engine)


    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(r"support\Interface\icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    app.setWindowIcon(icon)

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(_member_controller, _music_controller, _music_like_controller)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())





