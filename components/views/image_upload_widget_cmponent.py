from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Компонент страницы
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # Отображение загруженной обложки курса
        self.preview_image = page.get_by_test_id(f"{identifier}-image-upload-widget-preview-image")

        # Блок загрузки/удаления обложки курса
        self.image_upload_info_icon = page.get_by_test_id(f"{identifier}-image-upload-widget-info-icon")
        self.image_upload_info_title = page.get_by_test_id(
            f"{identifier}-image-upload-widget-info-title-text")
        self.image_upload_info_description = page.get_by_test_id(
            f"{identifier}-image-upload-widget-info-description-text")

        self.upload_button = page.get_by_test_id(
            f"{identifier}-image-upload-widget-upload-button")
        self.upload_input = page.get_by_test_id(
            f"{identifier}-image-upload-widget-input")
        self.remove_button = page.get_by_test_id(
            f"{identifier}-image-upload-widget-remove-button")

    def check_visible(self, is_uploaded_image: bool = False):
        expect(self.image_upload_info_icon).to_be_visible()

        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text("Recommended file size 540X300")

        expect(self.upload_button).to_be_visible()

        if is_uploaded_image:
            expect(self.preview_image).to_be_visible()
            expect(self.remove_button).to_be_visible()
        else:
            self.preview_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here"
            )

    def upload_preview_image(self, file_path: str):
        self.upload_input.set_input_files(file_path)

    def click_remove_image_button(self):
        self.remove_button.click()
