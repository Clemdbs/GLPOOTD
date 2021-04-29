from PyQt5 import QtCore, QtGui, QtWidgets
from vue.admin_vue import Ajout_musique
from model.database import DatabaseEngine
from controller.music_controller import MusicController
import sys

if __name__ == "__main__":
    # La table de données liée au compte utilisateur
    database_engine = DatabaseEngine(url='sqlite:///musique.db')
    database_engine.create_database()

    _music_controller = MusicController(database_engine)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ajout_musique(_music_controller)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())