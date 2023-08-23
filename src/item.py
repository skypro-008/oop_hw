import csv


class Item:
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception('Длина товара превышает 10 символов.')
        self.__name = value

    @classmethod
    def from_csv(cls, filename):
        with open(filename) as fp:
            items = csv.DictReader(fp)
            for item in items:
                name = item['name']
                price = float(item['price'])
                if cls.is_integer(price):
                    price = int(price)

                quantity = int(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def is_integer(num) -> bool:
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item1
    print(item1)
    # print(item1.calculate_total_price())
    # print(item2.calculate_total_price())
    #
    # Item.pay_rate = 0.8
    # item1.apply_discount()
    # print(item1.price)
    # print(item2.price)
    #
    # print(Item.all)
