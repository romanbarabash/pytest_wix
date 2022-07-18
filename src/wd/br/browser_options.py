from selenium import webdriver

from config import DEBUG, DOWNLOADS_DIR
from src.utils import get_path
from src.wd.br.browser_manger import browser_manager

DEFAULT_BROWSER_NAME = 'default'


def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    if not DEBUG:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

    # profile = {'plugins.always_open_pdf_externally': True,
    #            'download.default_directory': get_path(DOWNLOADS_DIR),
    #            'download.prompt_for_download': False}
    #
    # options.add_experimental_option('prefs', profile)
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    return options


def open_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    browser_manager.open_browser(webdriver.Chrome(options=get_options()), browser_name)
    browser_manager.driver.implicitly_wait(0)  # should be zero


def close_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    browser_manager.close_browser(browser_name)
