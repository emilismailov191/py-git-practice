class User:
    """Класс пользователя."""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def describe(self):
        return f"Пользователь: {self.name}, Email: {self.email}"