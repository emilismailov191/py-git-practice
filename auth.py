class Auth:
    """Класс для проверки данных пользователя."""

    def login(self, user, email):
        return user.email == email