from abc import ABC, abstractmethod
import math

"""
Саченко Владислав Олегович, ИП-91, В-22, задания А и В
Работа выполнена на языке программирования Python
"""


class Function(ABC):
    # Абстрактный класс "функции"

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, value):
        if not isinstance(value, int):
            raise ValueError('Value is not a number')
        self._variable = value

    @abstractmethod
    def count(self):
        # Виртуальный метод подсчета функции
        raise NotImplementedError("Subclass must implement abstract method")


class Sin(Function):

    def __init__(self, variable):
        self.variable = variable

    def count(self):
        # Переопределненный метод для синуса
        gradus = self.variable % (360)
        self.variable = gradus/180*math.pi
        i, lasts, s, fact, num, sign = 1, 0, self.variable, 1, self.variable, 1
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= self.variable * self.variable
            sign *= -1
            s += num / fact * sign
        return +s


class Cos(Function):
    def __init__(self, variable):
        self.variable = variable

    def count(self):
        # Переопределненный метод для косинуса
        gradus = self.variable % (360)
        self.variable = gradus/180*math.pi
        i, lasts, fact, num, sign = 0, 0, 1, self.variable, 1
        s = self.variable**i
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i)
            num *= self.variable * self.variable
            sign *= -1
            s += num / fact * sign
        return +s


sinus = Sin("90")
sinus.count()
