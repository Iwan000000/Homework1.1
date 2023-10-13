from item import Item

if __name__ == "__main__":
    item1 = Item("Ноутбук", 1000, 5)
    item2 = Item("Мышка", 500, 10)
    print(item1.total_cost())  # Выводит без скидки
    print(item2.total_cost())  # Выводит без скидки

    Item.apply_discount(0.15)  # Установка скидки в 15%

    print(item1.total_cost())  # Выводит со скидкой
    print(item2.total_cost())  # Выводит со скидкой
