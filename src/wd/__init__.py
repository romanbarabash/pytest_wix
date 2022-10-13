from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.wd.browser.browser_manager import browser_manager
from src.wd.elements import Locator, Element, Collection

__all__ = {'element', 'collection'}


def element(by: Tuple[By, str]) -> Element:
    driver = lambda: browser_manager.driver
    return Element(Locator(f'element{by}', lambda: driver().find_element(*by)))


def collection(by: Tuple[By, str]) -> Collection:
    driver = lambda: browser_manager.driver
    return Collection(Locator(f'collection{by}', lambda: driver().find_elements(*by)))

