import difflib
import functools
import os
import time
from abc import ABCMeta, abstractmethod
from pathlib import Path

from config import TIMEOUT, POLLING
from src.browser_manager.browser_manager import browser_manager


class Pattern(metaclass=ABCMeta):
    @abstractmethod
    def get_red_text(self, text: str) -> str:
        pass

    @abstractmethod
    def get_green_text(self, text: str) -> str:
        pass


class CompareString:

    def __init__(self,
                 actual_text: str,
                 expected_text: str,
                 trim_extra_space: bool = False,
                 trim_comma: bool = False,
                 trim_newline: bool = False,
                 case_insensitive: bool = False):
        self.__trim_extra_space = trim_extra_space
        self.__trim_comma = trim_comma
        self.__trim_newline = trim_newline
        self.__case_insensitive = case_insensitive

        self._actual_text = actual_text
        self._expected_text = expected_text

    def _format_text(self, text: str) -> str:
        if self.__trim_comma:
            text = text.replace(',', '')
        if self.__trim_newline:
            text = text.replace('\n', ' ')
        if self.__trim_extra_space:
            text = ' '.join(text.split())
        if self.__case_insensitive:
            text = text.lower()
        return text

    def _compare_text(self, pattern: Pattern) -> str:
        diff = difflib.ndiff(self._expected_text.split(), self._actual_text.split())

        compared_text = []
        for word in diff:
            if word.startswith('- '):
                compared_text.append(pattern.get_red_text(word[2:]))
            elif word.startswith('+ '):
                compared_text.append(pattern.get_green_text(word[2:]))
            elif word.startswith('? '):
                continue
            else:
                compared_text.append(word[2:])
        compared_text = ' '.join(compared_text)

        if isinstance(pattern, HTMLPattern):
            return pattern.get_font_family_text(compared_text)

        return compared_text

    @property
    def is_equal(self) -> bool:
        return self._format_text(self._actual_text) == self._format_text(self._expected_text)

    @property
    def is_contain(self):
        return self._format_text(self._expected_text) in self._format_text(self._actual_text)

    def get_console_text(self) -> str:
        return f'Wrong text\n\n' \
               f'Actual:\n{self._actual_text}\n\n' \
               f'Expected:\n{self._expected_text}'

    def get_compared_console_text(self) -> str:
        pattern = ConsolePattern()
        return self._compare_text(pattern)


class ConsolePattern(Pattern):
    def get_red_text(self, text: str) -> str:
        return '\033[91m' + text + '\033[0m'

    def get_green_text(self, text: str) -> str:
        return '\033[92m' + text + '\033[0m'


class HTMLPattern(Pattern):
    def get_red_text(self, text: str) -> str:
        return '<span style="color:red">' + text + '</span>'

    def get_green_text(self, text: str) -> str:
        return '<span style="color:green">' + text + '</span>'

    def get_font_family_text(self, text: str) -> str:
        return f'<div style="font-family:monospace;font-size:1em;">{text}</div>'


def get_root_folder() -> Path:
    return Path(__file__).parent.parent.absolute()


def get_path(*path) -> str:
    return os.path.join(get_root_folder(), *path)


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
