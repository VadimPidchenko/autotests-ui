from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.name = name
        self.locator = locator
        self.page = page

    def get_locator(self, **kwargs) -> Locator:
        """
        Метод для инициализации локатора с динамической подстановкой значений в него.

        :param kwargs: Аргументы для подставновки в локатор.
        :return: Объект Locator.
        """
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        """
        Клик на элемент.
        """
        locator = self.get_locator(**kwargs)
        locator.click()

    def check_visible(self, **kwargs):
        """
        Проверка видимости элемента.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        """
        Проверка наличия текста у элемента.
        """
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)
