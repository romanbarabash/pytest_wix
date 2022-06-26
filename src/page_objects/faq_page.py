from src.page_elements.faq_page_elements import FAQPageElements
from src.page_objects.base_page import BasePage


class FAQPage(BasePage):
    PATH = 'faq'

    def __init__(self):
        super().__init__()

        self.faq_page_elements = FAQPageElements()
