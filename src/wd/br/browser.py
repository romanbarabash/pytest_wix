from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.wd.br.browser_manger import browser_manager
from src.wd.elements import Locator, Element, Collection

__all__ = ['browser']


class _Browser:

    @property
    def driver(self) -> WebDriver:
        return browser_manager.driver

    def open_url(self, url: str):
        self.driver.get(url)
        return self

    def refresh_page(self):
        self.driver.refresh()

    def element(self, by: Tuple[By, str]) -> Element:
        driver = lambda: self.driver
        return Element(Locator(f'element{by}', lambda: driver().find_element(*by)))

    def collection(self, by: Tuple[By, str]) -> Collection:
        driver = lambda: self.driver
        return Collection(Locator(f'collection{by}', lambda: driver().find_elements(*by)))


browser = _Browser()
