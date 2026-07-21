from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):

    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator("input")

    def fill(self, text: str, **kwargs):
        """
        Заполнение поля текстом.
        """
        locator = self.get_locator(**kwargs)
        locator.fill(text)

    def check_have_value(self, value: str, **kwargs):
        """
        Проверка наличия значения в поле.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
