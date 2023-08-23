from src.keyboard import Keyboard


def test_mixin_default_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"


def test_mixin_lang_switch():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"

    kb.change_lang()
    assert kb.language == "RU"
