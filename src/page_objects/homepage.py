import allure

from src.page_elements.homepage_elements import HomepageElements
from src.page_objects.base_page import BasePage


class HomePage(BasePage):
    PATH = ''

    def __init__(self):
        super().__init__()

        self.homepage_elements = HomepageElements()

    def click_shop_now_button(self):
        with allure.step('Click "Shop Now" button'):
            self.homepage_elements.shop_now_button.click()
        return self
