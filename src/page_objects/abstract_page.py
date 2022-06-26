from abc import ABCMeta
from urllib.parse import urljoin

from hamcrest import assert_that, contains_string

from src.wd.br.browser import browser


class AbstractPage(metaclass=ABCMeta):

    def open(self, host: str, path: str | bool) -> 'AbstractPage':
        url = urljoin(host, path)
        browser.open_url(url)
        return self

    def verify_current_url(self, partial_url):
        assert_that(browser.current_url, contains_string(str(partial_url)), 'Verify url contains text')
        return self

    def refresh_page(self) -> 'AbstractPage':
        browser.driver.refresh()
        return self
