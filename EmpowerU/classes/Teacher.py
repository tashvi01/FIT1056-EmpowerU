from classes.User import User

class Admin(User):
    def __init__(self, id, password, username):
        self.id = id
        self.password = password
        self.username = username