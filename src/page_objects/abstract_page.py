from abc import ABCMeta
from urllib.parse import urljoin

from hamcrest import assert_that, contains_string

from src.wd.br.browser import browser


class AbstractPage(metaclass=ABCMeta):

    def _join_url(self, host: str, path: str | bool):
        return urljoin(host, path)

    def open(self, host: str, path: str | bool) -> 'AbstractPage':
        browser.open_url(self._join_url(host, path))
        return self

    def verify_current_url(self, partial_url):
        assert_that(browser.current_url, contains_string(str(partial_url)), 'Verify url contains text')
        return self

    def refresh_page(self) -> 'AbstractPage':
        browser.driver.refresh()
        return self
