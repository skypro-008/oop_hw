from src.item import Item
from src.mixins import LangMixin


class Keyboard(Item, LangMixin):
    def __init__(self, name, price, quality) -> None:
        super().__init__(name, price, quality)
        LangMixin.__init__(self)
