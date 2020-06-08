from goods import *
from database import *

catalog = Catalog()
catalog.read_base()
customer_base = CustomerBase()

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
    catalog.show()
    name = str(input("Введите ваше имя: "))
    if customer_base.in_base(name):
        pass
    else:


goods.print()
