from abc import ABCMeta
from urllib.parse import urljoin

from src.webdriver.browser_manager import browser_manager


class AbstractPage(metaclass=ABCMeta):

    def _join_url(self, host: str, path: str):
        return urljoin(host, path)

    def open(self, host: str, path: str) -> 'AbstractPage':
        browser_manager.open_url(self._join_url(host, path))
        return self
