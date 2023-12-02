from config import USERS

class User():
    def checkPassword(self, password):
        return self in USERS and USERS[self] == password