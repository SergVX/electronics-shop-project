"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def computer():
    Item.pay_rate = 0.90
    return Item("Computer", 80000, 3)


def test_item_init(computer):
    """ Создаем экземпляр класса Item"""
    assert computer.price == 80000


def test_item_calculate_total_price(computer):
    """ Проверяем стоимость всех товаров в магазине данного экземпляра"""
    assert computer.calculate_total_price() == 240000


def test_item_apply_discount(computer):
    """ Проверяем применение скидки к данному экземпляру"""
    computer.apply_discount()
    assert computer.price == 72000.0
