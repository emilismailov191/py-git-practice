class Student:
    """Класс для хранения информации о студенте."""
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def describe(self):
        return f"{self.name}, группа {self.group}, средний балл {self.average_grade}"
