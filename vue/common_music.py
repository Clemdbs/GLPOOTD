import re

class Common_music:

    def ask(self, key_name: str = ""):
        message = "Entrer %s" % key_name
        message += ": "
        string = input(message).rstrip()
        return string

    def ask_titre(self, default=None):
        return self.ask(key_name="titre")

    def ask_artiste(self, default=None):
        return self.ask(key_name="artiste")

    def ask_album(self, default=None):
        return self.ask(key_name="album")