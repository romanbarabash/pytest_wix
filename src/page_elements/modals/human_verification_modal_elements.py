from src.elements_manager import element, by


class HumanVerificationModalElements:
    def __init__(self):
        self._root_element = element(by.xpath('//*[@data-testid="captcha-dialog"]'))

        self.title = self._root_element.element(by.xpath('.//h2'))
        self.content = self._root_element.element(by.xpath('.//*[@data-testid="subtitle"]'))
