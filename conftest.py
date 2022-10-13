from enum import Enum

import pytest

from config import SCREENSHOTS_DIR
from src.utils import get_path
from src.webdriver.browser.browser_manager import browser_manager


class Status(Enum):
    PASSED = 'passed'
    FAILED = 'failed'
    SKIPPED = 'skipped'


class TestCaseStatus:
    __status = None

    @classmethod
    def set(cls, status: Status):
        cls.__status = status

    @classmethod
    def is_failed(cls) -> bool:
        return cls.__status == Status.FAILED


def pytest_report_teststatus(report):
    if report.when == 'call':
        if report.failed or report.outcome == 'rerun':
            TestCaseStatus.set(Status.FAILED)
        elif report.skipped:
            TestCaseStatus.set(Status.SKIPPED)
        else:
            TestCaseStatus.set(Status.PASSED)


@pytest.fixture
def on_fail(request):
    def screenshot():
        if TestCaseStatus.is_failed():
            browser_manager.attach_screenshot_and_logs()
            browser_manager.save_screenshot(get_path(SCREENSHOTS_DIR), request.node.name)

    request.addfinalizer(screenshot)
