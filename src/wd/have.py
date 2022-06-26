from typing import Union

from src.wd.conditions import ValueElementCondition


def value(value: Union[int, str], trim_extra_space=False, trim_comma=False, trim_newline=False, case_insensitive=False) -> ValueElementCondition:
    return ValueElementCondition(value=value,
                                 trim_extra_space=trim_extra_space,
                                 trim_comma=trim_comma,
                                 trim_newline=trim_newline,
                                 case_insensitive=case_insensitive)
