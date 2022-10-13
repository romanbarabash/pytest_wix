from __future__ import annotations

import time
from typing import List, Generic, Callable, TypeVar, Tuple, Union, Iterator, Optional

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from config import TIMEOUT, POLLING
from src.exception_handler import retry, handle_exception
from src.webdriver.browser_manager import browser_manager
from src.webdriver.conditions import BaseCondition

T = TypeVar('T')

__all__ = ['Element', 'Collection', 'Locator']



def wait_for(element: Union[Element, Collection], condition: BaseCondition, timeout: int, polling: float, strict: bool):
    end_time = time.time() + timeout
    while True:
        try:
            condition.match(element)
            break
        except Exception as e:  # pylint: disable=W0703
            if time.time() > end_time:
                if not strict:
                    return
                raise handle_exception(e) from None
            time.sleep(polling)


class Locator(Generic[T]):
    def __init__(self, description: str, locate: Callable[[], T]):
        self._description = description
        self._locate = locate

    def __call__(self) -> T:
        return self._locate()

    def __str__(self) -> str:
        return self._description


class BaseElement:
    @property
    def driver(self) -> WebDriver:
        return browser_manager.driver


class Element(BaseElement):
    def __init__(self, locator: Locator[WebElement]):
        self._locator = locator

    def __str__(self) -> str:
        return str(self._locator)

    def __call__(self) -> WebElement:
        with allure.step(f'Find "{self}"'):
            return self._locator()

    def element(self, by: Tuple[By, str]) -> Element:
        return Element(Locator(f'{self}.element{by}', lambda: self().find_element(*by)))

    def collection(self, by: Tuple[By, str]) -> Collection:
        return Collection(Locator(f'{self}.collection{by}', lambda: self().find_elements(*by)))

    @property
    def parent(self) -> Element:
        return Element(Locator(f'{self}.parent', lambda: self().find_element(By.XPATH, '..')))

    @retry(timeout=TIMEOUT, polling=POLLING)
    def click(self, force=False) -> Element:
        element = self()
        with allure.step(f'Click "{self}", force = {force}'):
            if not force:
                element.click()
            else:
                action = ActionChains(self.driver)
                action.move_to_element(element).click().perform()
        return self

    @retry(timeout=TIMEOUT, polling=POLLING)
    def check(self, value: Optional[bool] = None) -> Element:
        with allure.step(f'Check "{self}" to have value {value}'):
            element = self()
            if value is None:
                self.click(force=True)
            elif not value and element.is_selected():
                self.click(force=True)
            elif value and not element.is_selected():
                self.click(force=True)
        return self


    @retry(timeout=TIMEOUT, polling=POLLING)
    def clear(self) -> Element:
        with allure.step(f'Clear "{self}"'):
            element = self()
            element.send_keys(Keys.CONTROL + "a", Keys.DELETE)
        return self

    @retry(timeout=TIMEOUT, polling=POLLING)
    def send_keys(self, value: str, clean: bool = True) -> Element:
        element = self()
        with allure.step(f'Send keys "{value}" clean "{clean}" "{self}"'):
            if clean:
                element.send_keys(Keys.CONTROL + "a", Keys.DELETE)
            element.send_keys(value)
        return self


    def should(self, condition: BaseCondition, timeout: int = TIMEOUT, polling: float = POLLING, strict: bool = True) -> Element:
        wait_for(self, condition, timeout, polling, strict)
        return self

    @property
    @retry(timeout=TIMEOUT, polling=POLLING)
    def text(self) -> str:
        return self().text

    @property
    @retry(timeout=TIMEOUT, polling=POLLING)
    def value(self) -> str:
        return self().get_attribute('value')

    def is_enabled(self) -> bool:
        return self().is_enabled()

    def is_displayed(self) -> bool:
        return self().is_displayed()

    @retry(timeout=TIMEOUT, polling=POLLING)
    def is_selected(self) -> bool:
        return self().is_selected()

    def is_exists(self) -> bool:
        try:
            self()
            return True
        except NoSuchElementException:
            return False


class Collection(BaseElement):
    def __init__(self, locator: Locator[List[WebElement]]):
        self._locator = locator

    def __str__(self) -> str:
        return str(self._locator)

    def __call__(self) -> List[WebElement]:
        return self._locator()

    def __len__(self) -> int:
        return len(self())

    def __iter__(self) -> Iterator[Element]:
        web_elements = self()
        cached = Collection(Locator(f'{self}.cached', lambda: web_elements))

        for i in range(len(cached())):
            element = cached[i]
            yield element

    def __getitem__(self, index: int) -> Element:
        return self.element(index)

    def element(self, index: int) -> Element:
        def find() -> WebElement:
            web_elements = self()
            length = len(web_elements)

            if length <= index:
                raise AssertionError(
                    f'Cannot get element with index {index} ' +
                    f'from web_elements collection with length {length}')

            return web_elements[index]

        return Element(Locator(f'{self}[{index}]', find))

    @property
    def first(self) -> Element:
        return self.element(0)

    @property
    def last(self) -> Element:
        return self.element(-1)

    def should(self,
               condition: BaseCondition,
               timeout: int = TIMEOUT,
               polling: float = POLLING,
               strict: bool = True) -> Collection:
        wait_for(self, condition, timeout, polling, strict)
        return self

    def size(self) -> int:
        return len(self())

    def is_enabled(self) -> bool:
        for element in self():
            if not element.is_enabled():
                return False
        return True

    def is_displayed(self) -> bool:
        for element in self():
            if not element.is_displayed():
                return False
        return True

    def is_selected(self) -> bool:
        for element in self():
            if not element.is_selected():
                return False
        return True

    def is_exists(self) -> bool:
        if self.size():
            return True
        return False
