class Teacher:
    """Класс для хранения информации о преподавателе."""
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def describe(self):
        return f"{self.name}, предмет {self.subject}, стаж {self.experience} лет"
