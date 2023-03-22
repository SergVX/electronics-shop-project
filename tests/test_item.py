"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def computer():
    return Item("Computer", 80000, 3)


def test_item_init(computer):
    """ Создаем экземпляр класса Item"""
    assert computer.name == "Computer"
    assert computer.price == 80000
    assert computer.quantity == 3
    assert computer.pay_rate == 1.0
    assert len(computer.all) == 1


def test_item_calculate_total_price(computer):
    """ Проверяем стоимость всех товаров в магазине данного экземпляра"""
    assert computer.calculate_total_price() == 240000


def test_item_apply_discount(computer):
    """ Проверяем применение скидки к данному экземпляру"""
    Item.pay_rate = 0.5
    computer.apply_discount()
    assert computer.price == 40000.0


def test_instantiate_from_csv(computer):
    """Тест метода instantiate_from_csv"""
    computer.instantiate_from_csv()
    assert len(computer.all) == 5


def test_string_to_number(computer):
    """Тест метода string_to_number"""
    assert computer.string_to_number('21') == 21
    assert computer.string_to_number('21.5') == 21
