import pytest

from src.item import Item, InstantiateCSVError


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_calculate_total_price(item) -> None:
    assert item.calculate_total_price() == 2000


def test_apply_discount(item) -> None:
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 800


def test_name_norm_len(item):
    item.name = 'Телефон'
    assert item.name == 'Телефон'


def test_name_too_long_len(item):
    """Название товара слишком длинное"""
    with pytest.raises(Exception):
        item.name = 'ТелефонТелефонТелефон'


def test_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv('tests/test_data/items.csv')
    assert len(Item.all) == 2

    assert Item.all[0].name == 'Товар 1'
    assert Item.all[0].price == 10
    assert Item.all[0].quantity == 5

    assert Item.all[1].name == 'Товар 2'
    assert Item.all[1].price == 20
    assert Item.all[1].quantity == 15


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.all = []
        Item.instantiate_from_csv('tests/test_data/nonexistent_items.csv')


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.all = []
        Item.instantiate_from_csv('tests/test_data/corrupted_items.csv')


def test_is_integer():
    assert Item.is_integer(10) is True
    assert Item.is_integer(10.0) is True
    assert Item.is_integer('10') is False
    assert Item.is_integer(None) is False


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 1000, 2)"


def test_str(item):
    assert str(item) == "Смартфон"


def test_add_items(item, phone):
    assert item + phone == 7
    assert phone + phone == 10


def test_add_items_error(item, phone):
    with pytest.raises(TypeError):
        item + 'phone'
    with pytest.raises(TypeError):
        phone + 1
