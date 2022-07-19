from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import DEBUG
from src.wd.br.browser_manger import browser_manager

DEFAULT_BROWSER_NAME = 'default'


def get_options():
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


def open_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    manager = ChromeDriverManager().install()
    init_webdriver = webdriver.Chrome(manager, options=get_options())
    browser_manager.open_browser(init_webdriver, browser_name)
    browser_manager.driver.implicitly_wait(0)  # should be zero


def close_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    browser_manager.close_browser(browser_name)
