import pytest


def test_phone_initialized(phone):
    assert phone.name == 'iPhone 14'
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_phone_number_of_sim_setter(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_phone_number_of_sim_setter_error(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1


def test_phone_add(phone):
    with pytest.raises(TypeError):
        phone + 'phone'
    with pytest.raises(TypeError):
        phone + 1
