from abc import ABCMeta

from src.page_objects.abstract_page import AbstractPage


class AbstractLoginPage(AbstractPage, metaclass=ABCMeta):

    def login(self, username: str, password: str) -> 'AbstractLoginPage':
        pass
