class Auth:
    def __init__(self):
        self.users = {}

    def register(self, user, password):
        if user.username in self.users:
            return False
        self.users[user.username] = password
        return True

    def authenticate(self, username, password):
        return self.users.get(username) == password
