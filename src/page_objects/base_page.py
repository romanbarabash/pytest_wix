import allure

from config import HOST
from src.page_elements.base_elements import BaseElements
from src.page_elements.modals.human_verification_modal_elements import HumanVerificationModalElements
from src.page_objects.abstract_page import AbstractPage
from src.webdriver import be


class HumanVerificationModal:
    def __init__(self):
        self.human_verification_modal_elements = HumanVerificationModalElements()

    def verify_presence_of_modal(self, is_present: bool = True):
        with allure.step(f'Verify "Human Verification Modal" present: {is_present}'):
            condition = be.visible() if is_present else be.not_exist()
            self.human_verification_modal_elements._root_element.should(condition)
        return self


class BasePage(AbstractPage):
    PATH = None

    def __init__(self):
        self.base_elements = BaseElements()

    def navigate(self):
        self.open(host=HOST, path=self.PATH)
        return self
