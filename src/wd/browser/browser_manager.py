from typing import Tuple

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config import CHROME_DRIVER_PATH, DEBUG
from src.wd.elements import Locator, Element, Collection

__all__ = ['browser_manager']


class _SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class BrowserManager(metaclass=_SingletonMeta):
    __current_driver = None

    def get_options(self):
        options = webdriver.ChromeOptions()
        if DEBUG:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
        else:
            options.add_argument("--start-maximized")
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

        return options

    def get_browser(self, web_driver: WebDriver) -> WebDriver:
        self.__current_driver = web_driver
        self.__current_driver.implicitly_wait(0)
        return self.__current_driver

    def open_browser(self):
        self.get_browser(webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=self.get_options()))

    def open_url(self, url: str):
        self.__current_driver.get(url)
        return self

    def close_browser(self):
        self.__current_driver.quit()

    def refresh_page(self):
        self.__current_driver.refresh()

    def element(self, by: Tuple[By, str]) -> Element:
        driver = lambda: self.__current_driver
        return Element(Locator(f'element{by}', lambda: driver().find_element(*by)))

    def collection(self, by: Tuple[By, str]) -> Collection:
        driver = lambda: self.__current_driver
        return Collection(Locator(f'collection{by}', lambda: driver().find_elements(*by)))


browser_manager = BrowserManager()