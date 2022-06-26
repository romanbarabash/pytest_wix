from abc import ABCMeta
from urllib.parse import urljoin

from src.page_objects.abstract_page import AbstractPage
from src.wd.br.browser import browser


class AbstractLoginPage(AbstractPage, metaclass=ABCMeta):

    def __init__(self, host: str, path: str):
        self.HOST = host
        self.PATH = path

    def open_page(self) -> 'AbstractLoginPage':
        url = urljoin(self.HOST, self.PATH)
        browser.open_url(url)
        return self

    def login(self, username: str, password: str) -> 'AbstractLoginPage':
        pass

