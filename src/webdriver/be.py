from src.webdriver.conditions import ExistElementCondition, \
    NotExistElementCondition, VisibleElementCondition, \
    InvisibleElementCondition, EnabledElementCondition, \
    DisabledElementCondition

__all__ = ['exist', 'not_exist',
           'visible', 'invisible',
           'enabled', 'disabled']


def exist() -> ExistElementCondition:
    return ExistElementCondition()


def not_exist() -> NotExistElementCondition:
    return NotExistElementCondition()


def visible() -> VisibleElementCondition:
    return VisibleElementCondition()


def invisible() -> InvisibleElementCondition:
    return InvisibleElementCondition()


def enabled() -> EnabledElementCondition:
    return EnabledElementCondition()


def disabled() -> DisabledElementCondition:
    return DisabledElementCondition()
