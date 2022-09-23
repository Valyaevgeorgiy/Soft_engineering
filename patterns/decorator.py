"""
Декоратор (Decorator, Wrapper) — паттерн, структурирующий объекты. Динамически добавляет объекту новые обязанности.
Является гибкой альтернативой порождению подклассов с целью расширения функциональности.

Шаблон «Декоратор» позволяет во время выполнения подключения к объекту дополнительного поведения
(статически или динамически) изменять поведение объекта, обёртывая его в объект класса «декоратора» и не влияя на
поведение других объектов того же класса.
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

    def __init__(self, student_model, points, password):
        self._student = student_model # Объект студента
        self._points = points
        self._password = password
        self._grade = ""

    def __getattr__(self, item):
        return getattr(self._student, item)

    def get_points(self):
        # расширяем функциональность объекта добавляя возможность регистрации при корректности баллов в ведомости
        is_registration = False
        if self._points < 50:
            is_registration = True
            self._grade = "не сдал"
        elif 50 <= self._points <= 69:
            is_registration = True
            self._grade = "удовлетворительно"
        elif 70 < self._points <= 84:
            is_registration = True
            self._grade = "хорошо"
        elif 85 < self._points <= 100:
            is_registration = True
            self._grade = "отлично"
        else:
            print(f"Сверьте, пожалуйста, ещё раз ведомость! Выходит {self._points} баллов(-а).")

        if is_registration and self._password:
            self._student._password = self._password
            print(f"Пользователь {self._student._surname} {self._student._name} успешно зарегестрирован!")
            print(f"Пароль: {self._student._password}")
            print(f"Баллы: {self._points}")
        else:
            print("Ещё раз сверьте ведомость при регистрации! И ещё раз проверьте ваш пароль на пустоту!")

student_new = Student("Сергей", "Трофимов", 22, 221201)

student_registration = Progress(student_new, random.randint(50, 95), 'qwerty')

student_registration.full_info()
student_registration.get_points()
