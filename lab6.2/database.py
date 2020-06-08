from abc import ABC, abstractmethod
from random import randint


def DataBase(ABC):
    @property
    def base(self):
        return self._base

    @price.setter
    def base(self, value):
        if not isinstance(value, list):
            raise ValueError('Price is not a number')
        self._base = value

    def read_base():
        file = open('customer_base.txt')
        f = file.readlines()
        for i in range(len(f)):
            self.base.append(i)

    def write_base():
        file = open('base.txt', 'w')
        for i in self.base:
            file.write(str(i))
        file.write('\n')

    def add(data):
        self.base.append(data)


class Catalog(DataBase):
    def __init__(self):
        self.base = list()

    def show():
        for i in self.base:
            print(i)

    def sold(key):
        item = self.base[key]
        self.base[key] = "SOLD"

    def return_item(key):
        return self.base[key]


class CustomerBase(DataBase):
    def __init__(self):
        self.base = list()

    def in_base(name):
        if name in self.base:
            return True
        else:
            return False


class Report(DataBase):
    def __init__(self):
        self.base = list()

    def write_base():
        file = open('base.txt', 'w')
        for i in self.base:
            file.write(str(i))
        file.write('\n')

    def append_deal(name, type, number):
        self.base.append([name, type, number])
