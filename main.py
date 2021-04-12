from vue.accueil_vue import Ui_Accueil
from model.database import DatabaseEngine

if __name__ == '__main__':
    #La table de données liée au compte utilisateur
    database_engine = DatabaseEngine(url='sqlite:///compte.db')
    database_engine.create_database()
    ui = Ui_Accueil(database_engine)
    ui.setupUi()
