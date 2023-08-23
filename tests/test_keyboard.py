from src.keyboard import Keyboard


def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_keyboard_language_switch():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"

    kb.change_lang()
    assert kb.language == "EN"

