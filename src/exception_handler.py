import functools
import time

from config import TIMEOUT, POLLING
from src.webdriver.browser_manager import browser_manager


def retry(timeout=TIMEOUT, polling=POLLING, screenshot: bool = True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            end_time = time.time() + timeout
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if time.time() > end_time:
                        raise handle_exception(e, screenshot) from None
                    time.sleep(polling)

        return wrapper

    return decorator


def handle_exception(e: Exception, screenshot: bool = True) -> AssertionError:
    if screenshot:
        pass
        browser_manager.attach_screenshot_and_logs()

    if isinstance(e, AssertionError):
        return e

    if hasattr(e, 'stacktrace'):
        e.stacktrace = None

    return AssertionError(e)
