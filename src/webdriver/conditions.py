from abc import ABCMeta, abstractmethod
from typing import Union

from src.utils import CompareString

__all__ = ['VisibleElementCondition', 'InvisibleElementCondition',
           'EnabledElementCondition', 'DisabledElementCondition',
           'NotExistElementCondition', 'ExistElementCondition',
           'ValueElementCondition']


class BaseCondition(metaclass=ABCMeta):
    @abstractmethod
    def match(self, element):
        pass


class VisibleElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert element.is_displayed(), 'Element is not displayed'


class InvisibleElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert not element.is_displayed(), 'Element is displayed'


class EnabledElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert element.is_enabled(), 'Element is not enabled'


class DisabledElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert not element.is_enabled(), 'Element is not disabled'


class NotExistElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert not element.is_exists(), 'Element should not exist'


class ExistElementCondition(BaseCondition):
    def match(self, element) -> None:
        assert element.is_exists(), 'Element should exist'


class ValueElementCondition(BaseCondition):
    def __init__(self, value: Union[str, int], trim_extra_space=False, trim_comma=False, trim_newline=False, case_insensitive=False):
        super().__init__()
        self.__trim_extra_space = trim_extra_space
        self.__trim_comma = trim_comma
        self.__trim_newline = trim_newline
        self.__case_insensitive = case_insensitive
        self._value = str(value)

    def match(self, element) -> None:
        compare_string = CompareString(element.value,
                                       self._value,
                                       self.__trim_extra_space,
                                       self.__trim_comma,
                                       self.__trim_newline,
                                       self.__case_insensitive)

        if not compare_string.is_equal:
            raise AssertionError(compare_string.get_compared_console_text())
