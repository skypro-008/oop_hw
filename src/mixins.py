class LangMixin:
    def __init__(self):
        """Default language is EN."""
        self.__language: str = 'EN'

    def change_lang(self) -> None:
        """Switch language between EN and RU."""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language
