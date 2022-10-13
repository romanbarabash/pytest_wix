from src.webdriver import element, by


class LoginPageElements:
    def __init__(self):
        self.login_button = element(by.xpath('//span[text()="Log In"]'))
        self.sign_in_login_switcher = element(by.xpath('//button[@data-testid="signUp.switchToSignUp"]'))
        self.login_with_email_button = element(by.xpath('//span[text()="Log in with Email"]'))
        self.email_field = element(by.xpath('//form[@data-testid="emailAuth"]//input[@type="email"]'))
        self.password_field = element(by.xpath('//form[@data-testid="emailAuth"]//input[@type="password"]'))
        self.email_login_button = element(by.xpath('//form[@data-testid="emailAuth"]//button[@data-testid="buttonElement"]'))
