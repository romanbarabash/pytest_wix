import base64
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

__all__ = ['browser_manager']


class _SingletonMeta(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class _BrowserManager(metaclass=_SingletonMeta):
    __browsers: Dict[str, WebDriver] = {}
    __current_browser: str = None

    def _close_browsers_with_exception(self, message: str):
        self.close_browsers()
        raise WebDriverException(message)

    def open_browser(self, web_driver: WebDriver, browser_name: str = 'default') -> str:
        if not isinstance(web_driver, WebDriver):
            self._close_browsers_with_exception('The attribute passed must be WebDriver')

        if browser_name in self.__browsers:
            self.__browsers['duplicate'] = web_driver
            self._close_browsers_with_exception(f'The browser with name: "{browser_name}" is already open')

        self.__browsers[browser_name] = web_driver
        self.__current_browser = browser_name

        return browser_name

    def get_current_browser(self) -> str:
        return self.__current_browser

    @property
    def driver(self) -> WebDriver:
        if not self.__browsers:
            raise WebDriverException('The browser is not open')

        return self.__browsers[self.__current_browser]

    def switch_to(self, browser_name: str):
        if browser_name not in self.__browsers:
            self._close_browsers_with_exception(f'The browser with name: "{browser_name}" is not open')

        self.__current_browser = browser_name

    def close_browser(self, browser_name: Optional[str] = None):
        if not browser_name:
            browser_name = self.__current_browser

        self.__browsers.pop(browser_name).quit()
        self.__current_browser = next(iter(self.__browsers), None)

    def close_browsers(self, *exclude):
        for key in list(self.__browsers):
            if key in exclude:
                continue

            self.__browsers.pop(key).quit()

        self.__current_browser = next(iter(self.__browsers), None)

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
                                                                            'clip': {'width': layout_metrics['contentSize']['width'],
                                                                                     'height': layout_metrics['contentSize']['height'],
                                                                                     'x': 0,
                                                                                     'y': 0,
                                                                                     'scale': 1}
                                                                            })

        return base64.b64decode(screenshot['data'])


browser_manager = _BrowserManager()
