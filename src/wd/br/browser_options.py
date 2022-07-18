from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import DEBUG
from src.wd.br.browser_manger import browser_manager

DEFAULT_BROWSER_NAME = 'default'


def get_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugin-port=9222")
    options.add_argument("--screen-size=1200x800")

    # profile = {'plugins.always_open_pdf_externally': True,
    #            'download.default_directory': get_path(DOWNLOADS_DIR),
    #            'download.prompt_for_download': False}
    #
    # options.add_experimental_option('prefs', profile)
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    return options


def open_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    init_webdriver = webdriver.Chrome(ChromeDriverManager().install(),
                                      desired_capabilities=get_options().to_capabilities())
    browser_manager.open_browser(init_webdriver, browser_name)
    browser_manager.driver.implicitly_wait(0)  # should be zero


def close_browser(browser_name: str = DEFAULT_BROWSER_NAME):
    browser_manager.close_browser(browser_name)
