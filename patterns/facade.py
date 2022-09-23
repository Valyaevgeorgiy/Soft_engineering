"""
Фасад (Facade) — паттерн, позволяющий структурировать объекты.

Предоставляет унифицированный интерфейс вместо набора интерфейсов некоторой подсистемы.
Фасад определяет интерфейс более высокого уровня, который упрощает использование подсистемы.

«Фасад» — это объект для более крупного тела кода (библиотеки классов), предоставляющий упрощённый интерфейс,
который скрывает сложность системы путём сведения всех возможных внешних вызовов к одному объекту,
делегирующему их соответствующим объектам системы.
"""

import random

class Student:
    """Студент вуза"""
    def __init__(self, name, surname, age, ticket_number):
        self._name = name
        self._surname = surname
        self._age = age
        self._ticket_number = ticket_number

    def full_info(self):
        print(f"Привет, меня зовут {self._surname} {self._name}.")
        print(f"Мне {self._age}, являюсь студентом с номером студенческого билета {self._ticket_number}.")

class Progress(object):
    """Успеваемость по обучению"""

    def __init__(self, points):
        self._points = points

    def get_points(self):
        if self._points < 50:
            print(f"{self._points} => оценка «не сдал» за предмет.")
        elif 50 <= self._points <= 69:
            print(f"{self._points} => оценка «удовлетворительно» за предмет.")
        elif 70 < self._points <= 84:
            print(f"{self._points} => оценка «хорошо» за предмет.")
        elif 85 < self._points <= 100:
            print(f"{self._points} => оценка «отлично» за предмет.")
        else:
            print(f"Сверьте, пожалуйста, ещё раз ведомость! Выходит {self._points} баллов(-а).")

class Facade(object):
    def __init__(self):
        self._stud = Student("Сергей", "Трофимов", 22, 221201)
        self._progress = Progress(random.randint(40, 110))

    def check_progress(self):
        self._stud.full_info()
        self._progress.get_points()

f = Facade()
f.check_progress()