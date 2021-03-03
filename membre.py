from user import *

class Membre:
    def __init__(self):
        self.liste_membre = []
        self.nb_membre = 0
    def ajouter_membre(self, utilisateur):
        self.liste_membre.append(utilisateur)
    def modif_membre(self, utilisateur):
        print("Que voulez-vous modifier ?")
        '''
        '''
    def print_membre(self):
        print(self.liste_membre)
