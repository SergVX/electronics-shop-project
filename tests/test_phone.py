import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_1():
    return Phone("Samsung_S9", 50000, 10, 2)


def test_item_init(phone_1):
    """ Создаем экземпляр класса Phone"""
    assert phone_1.name == "Samsung_S9"
    assert phone_1.price == 50000
    assert phone_1.quantity == 10
    assert phone_1.pay_rate == 1.0
    assert len(phone_1.all) == 1
    assert phone_1.number_of_sim == 2


def test_number_of_sim_setter(phone_1):
    """Тест сеттера атрибута number_of_sim"""

    phone_1.number_of_sim = 3
    assert phone_1.number_of_sim == 3
    try:
        phone_1.number_of_sim = 0.5
    except ValueError:
        pass


def test_repr(phone_1):
    """тест метода __repr__"""
    assert repr(phone_1) == "Phone('Samsung_S9', 50000, 10, 2)"

