import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1_000, 2)


@pytest.fixture
def phone() -> Phone:
    return Phone("iPhone 14", 120_000, 5, 2)
