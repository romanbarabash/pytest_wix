from src.webdriver import element, by


class FAQPageElements:
    def __init__(self):
        self.help_center_header = element(by.xpath('//*[text()="Help Center"]'))
