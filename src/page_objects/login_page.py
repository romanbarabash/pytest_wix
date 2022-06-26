from time import sleep

from config import HOST, USER_EMAIL, USER_PASSWORD
from src.page_elements.login_page_elements import LoginPageElements
from src.page_objects.abstract_login_page import AbstractLoginPage
from src.wd import be


class LoginPage(AbstractLoginPage):
    PATH = ''

    def __init__(self):
        super().__init__(HOST, self.PATH)

        self.login_elements = LoginPageElements()

    def sign_in(self, username: str, password: str) -> 'LoginPage':
        self.open_page()
        self.login(username, password)
        return self

    def login(self, username: str, password: str) -> 'LoginPage':
        # TODO handle issue with tremblin UI after page load
        sleep(2)
        self.login_elements.login_button.should(be.visible()).click()
        self.login_elements.sign_in_login_switcher.should(be.visible()).click()
        self.login_elements.login_with_email_button.click()
        self.login_elements.email_field.send_keys(USER_EMAIL)
        self.login_elements.password_field.send_keys(USER_PASSWORD)
        self.login_elements.email_login_button.click()

        return self
