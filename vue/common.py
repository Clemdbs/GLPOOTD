import re

class Common:

    def ask(self, key_name: str = ""):
        message = "Entrer %s" % key_name
        message += ": "
        string = input(message).rstrip()
        return string

    def ask_email(self, default=None):
        print("ok")
        return self.ask(key_name="email")