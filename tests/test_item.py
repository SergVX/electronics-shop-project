"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def computer():
    return Item("Computer", 80000, 3)
@pytest.fixture
def laptop():
    return Item("laptop", 150000, 5)

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


def test_repr(computer):
    """Тест метода __repr__"""
    assert computer.__repr__() == "Item('Computer', 80000, 3)"


def test_str(computer):
    """Тест метода __str__"""
    assert computer.__str__() == 'Computer'

def test_add(computer, laptop):
    """Тест метода сложения"""
    assert computer + laptop == 8
    assert computer + 3 == 'Cложение возможно только с экземплярами класса Item и дочерними классами'
