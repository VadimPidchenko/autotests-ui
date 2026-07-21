from elements.base_element import BaseElement


class FileInput(BaseElement):

    def set_input_files(self, files: str, **kwargs):
        """
        Метод для загрузки файлов.
        """
        locator = self.get_locator(**kwargs)
        locator.set_input_files(files)
