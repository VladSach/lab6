from abc import ABC, abstractmethod
from random import randint


class Goods(ABC):
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise ValueError('Price is not a number')
        self._price = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, int):
            raise ValueError('Time is not a number')
        self._time = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError('Description is not a string')
        self._description = value

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        if not isinstance(value, tuple):
            raise ValueError('Conditions is not a tuple')
        self._conditions = value

    @abstractmethod
    def count(self):
        raise NotImplementedError("Subclass must implement abstract method")


class SellNow(Goods):
    def __init__(self, price, time, description, conditions):
        self.price = price
        self.time = time
        self.description = description
        self.conditions = conditions

    def print(self):
        print(self.price, self.time, self.description, self.conditions)

    def count():
        return 0


class PutOnSale(Goods):
    def __init__(self, price, time, description, conditions):
        self.price = price
        self.time = time
        self.description = description
        self.conditions = conditions

    def print(self):
        print(self.price, self.time, self.description, self.conditions)

    def count():
        return 0


class DealSale(Goods):
    def __init__(self, price, time, description, conditions):
        self.price = price
        self.time = time
        self.description = description
        self.conditions = conditions

    def print(self):
        print(self.price,  self.description)

    def count():
        return 0


seller = bool(input("Вы покупатель(0) или продавец(1)? "))
if seller:
    type_of_goods = int(
        input('Выберити тип продажи: Продать сразу(1), выставить на аукцион(2), договорной(3): '))
    if type_of_goods == 1:
        price = int(input("Укажите цену в гривнах: "))
        time = int(input("Укажите на сколько часов вы хотети выставить товар: "))
        description = str(input("Опишите товар: "))
        conditions = tuple(
            input("Укажите условия доставки в формате \"стоимость, срок(кол-во дней), тип\": ").split(', '))
        goods = SellNow(price, time, description, conditions)
    elif type_of_goods == 2:
        price = int(input("Укажите цену в гривнах: "))
        time = int(input("Укажите на сколько часов вы хотети выставить товар: "))
        description = str(input("Опишите товар: "))
        conditions = tuple(
            input("Укажите условия доставки в формате \"стоимость, срок(кол-во дней), тип\": ").split(', '))
        goods = PutOnSale(price, time, description, conditions)
    elif type_of_goods == 3:
        price = int(input("Укажите цену в гривнах: "))
        time = randint(1, 8)
        description = str(input("Опишите товар: "))
        conditions = ('-', '-', '-')
        goods = DealSale(price, time, description, conditions)
    else:
        print('Неверный формат')
else:
    pass


goods.print()
