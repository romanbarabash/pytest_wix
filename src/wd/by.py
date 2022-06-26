from typing import Tuple

from selenium.webdriver.common.by import By

__all__ = ['css', 'xpath', 'text', 'partial_text']


def css(locator: str) -> Tuple[By, str]:
    return By.CSS_SELECTOR, locator


def xpath(locator: str) -> Tuple[By, str]:
    return By.XPATH, locator


def text(text: str, attribute: str = '*') -> Tuple[By, str]:
    return xpath(f'//{attribute}[normalize-space(text())="{text}"]')


def partial_text(partial_text: str, attribute: str = '*') -> Tuple[By, str]:
    return xpath(f'//{attribute}[contains(normalize-space(text()), "{partial_text}")]')
