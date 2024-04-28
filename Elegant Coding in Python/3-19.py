"""类定义"""
import datetime


class Employee(Person):
    POSITIONS = ['CEO', 'CTO', 'CFO', 'COO', 'CMO', 'CIO']

    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self.age = None
        self._age_last_calculated = None
        self._recalculated_age()

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Department: {self.department}"

    @classmethod
    def no_position_allowed(cls, position):
        return [t for t in cls.POSITIONS if t != position]

    @staticmethod
    def c_position(position):
        return position.lower()

    @property
    def id_with_name(self):
        return self.id, self.name

    def age(self):
        if datetime.date.today() > self._age_last_calculated:
            self._recalculated_age()
        return self.age

    def _recalculated_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        if today < datetime.date(today.year, self.birthday.month, self.birthday.day):
            age -= 1
        self.age = age
        self._age_last_calculated = today
