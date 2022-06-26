from src.wd.br.browser import browser
from src.wd.br.browser_manger import browser_manager

__all__ = {'browser_manager', 'browser', 'element', 'collection'}

element = browser.element
collection = browser.collection
