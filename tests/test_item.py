import pytest

from src.item import Item


def test_total_cost():
    item1 = Item("Ноутбук", 1000, 5)
    assert item1.total_cost() == 5000

    item2 = Item("Мышка", 200, 3)
    assert item2.total_cost() == 600

def test_apply_discount():
    item1 = Item("Ноутбук", 1000, 5)
    item1.apply_discount(0.2)
    assert item1.total_cost() == 4000

    item2 = Item("Мышка", 200, 3)
    item2.apply_discount(0.1)
    assert item2.total_cost() == 540

if __name__ == "__main__":
    pytest.main()