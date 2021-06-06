class Session:
    def __init__(self):
        self.id_user = ""
        self.id_musique_en_cours = ""
        self.pseudo = ""

    def initialiser_user(self, id, pseudo):
        self.id_user = id
        self.pseudo = pseudo

    def actualiser_musique(self, id):
        self.id_musique_en_cours = id