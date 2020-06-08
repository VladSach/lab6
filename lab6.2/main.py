from goods import *
from database import *

"""
Саченко Владислав Олегович, ИП-91, В-22, задания А и В
Работа выполнена на языке программирования Python
"""

catalog = Catalog()
customer_base = CustomerBase()
report = Report()
catalog.read_base()
customer_base.read_base()

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
        add(goods)
    elif type_of_goods == 2:
        price = int(input("Укажите цену в гривнах: "))
        time = int(input("Укажите на сколько часов вы хотети выставить товар: "))
        description = str(input("Опишите товар: "))
        conditions = tuple(
            input("Укажите условия доставки в формате \"стоимость, срок(кол-во дней), тип\": ").split(', '))
        goods = PutOnSale(price, time, description, conditions)
        add(goods)
    elif type_of_goods == 3:
        price = int(input("Укажите цену в гривнах: "))
        time = randint(1, 8)
        description = str(input("Опишите товар: "))
        conditions = ('-', '-', '-')
        goods = DealSale(price, time, description, conditions)
        add(goods)
    else:
        print('Неверный формат')
else:
    name = str(input("Введите ваше имя: "))
    catalog.show()
    if not customer_base.in_base(name):
        customer_base.add(name)
    key = int(input('Введите номер желаемого товара: '))
    report.append_deal(name, catalog.return_item(key), 1)
    report.write_base()
