class Item:

    discount_rate = 1
    instances = []

    def __init__(self, name, price, quantity):
        """Вводные данные о товаре"""

        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.instances.append(self)

    def total_cost(self):
        """Стоимость товара"""

        return self.price * self.quantity * self.__class__.discount_rate

    @classmethod
    def apply_discount(cls, discount):
        """Процент скидки товара"""

        cls.discount_rate = 1 - discount

