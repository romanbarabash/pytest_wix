import base64
import json
from datetime import datetime
from pathlib import Path
from typing import Tuple

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config import CHROME_DRIVER_PATH, DEBUG
from src.wd.elements import Locator, Element, Collection

__all__ = ['browser_manager']


class _SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class BrowserManager(metaclass=_SingletonMeta):
    __current_driver = None

    def get_options(self):
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

    @property
    def driver(self) -> WebDriver:
        return self.__current_driver

    def open_browser(self) -> WebDriver:
        self.__current_driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,  options=self.get_options())
        self.__current_driver.implicitly_wait(0)
        return self.__current_driver

    def open_url(self, url: str):
        self.__current_driver.get(url)
        return self

    def close_browser(self):
        self.__current_driver.quit()

    def refresh_page(self):
        self.__current_driver.refresh()

    def element(self, by: Tuple[By, str]) -> Element:
        driver = lambda: self.__current_driver
        return Element(Locator(f'element{by}', lambda: driver().find_element(*by)))

    def collection(self, by: Tuple[By, str]) -> Collection:
        driver = lambda: self.__current_driver
        return Collection(Locator(f'collection{by}', lambda: driver().find_elements(*by)))

    def attach_screenshot_and_logs(self):
        current_window = self.driver.current_window_handle

        for tab_index, window_name in enumerate(self.driver.window_handles):
            self.driver.switch_to.window(window_name)

            allure.attach(body=self.get_full_size_screenshot(),
                          name=f'Screenshot, tab {tab_index + 1}{" (current tab)" if window_name == current_window else ""} {self.driver.current_url}',
                          attachment_type=AttachmentType.PNG)

        self.driver.switch_to.window(current_window)

        allure.attach(body=json.dumps(self.driver.get_log('browser'), indent=4),
                      name="Logs",
                      attachment_type=AttachmentType.TEXT)

    def save_screenshot(self, full_path, file_name: str = 'screenshot'):
        current_date_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name = f'{file_name}-{current_date_time}.png'
        path = Path(full_path, file_name)

        if not path.parent.exists():
            path.parent.mkdir()

        self.driver.save_screenshot(str(path))

    def get_full_size_screenshot(self):
        layout_metrics = self.driver.execute_cdp_cmd('Page.getLayoutMetrics', {})
        screenshot = self.driver.execute_cdp_cmd('Page.captureScreenshot', {'format': 'png',
                                                                            'captureBeyondViewport': True,
                                                                            'clip': {
                                                                                'width': layout_metrics['contentSize'][
                                                                                    'width'],
                                                                                'height': layout_metrics['contentSize'][
                                                                                    'height'],
                                                                                'x': 0,
                                                                                'y': 0,
                                                                                'scale': 1}
                                                                            })

        return base64.b64decode(screenshot['data'])


browser_manager = BrowserManager()
