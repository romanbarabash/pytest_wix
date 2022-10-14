from src.elements_manager import element, by


class HomepageElements:
    def __init__(self):
        self.celebrating_beauty_and_style_header = element(by.xpath('//span[text()="Celebrating Beauty and Style"]'))
        self.celebrating_beauty_and_style_body = element(by.xpath("//div[@id='comp-kqx6zupp7']"))
        self.shop_now_button = element(by.xpath('//span[text()="Shop Now"]'))
