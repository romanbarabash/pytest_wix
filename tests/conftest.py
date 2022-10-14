import pytest

from config import USER_EMAIL, USER_PASSWORD
from src.browser_manager.browser_manager import browser_manager
from src.page_objects.base_page import HumanVerificationModal
from src.page_objects.contact_us_page import ContactUsPage
from src.page_objects.faq_page import FAQPage
from src.page_objects.homepage import HomePage
from src.page_objects.login_page import LoginPage


# region pages


@pytest.fixture(scope='session')
def homepage() -> HomePage:
    return HomePage()


@pytest.fixture(scope='session')
def contact_us_page() -> ContactUsPage:
    return ContactUsPage()


@pytest.fixture(scope='session')
def faq_page() -> FAQPage:
    return FAQPage()


@pytest.fixture(scope='session')
def login_page() -> LoginPage:
    return LoginPage()


# endregion pages


# region modals
@pytest.fixture(scope='session')
def human_verification_modal() -> HumanVerificationModal:
    return HumanVerificationModal()


# endregion modals

@pytest.fixture
def open_browser():
    browser_manager.open_browser()
    yield
    browser_manager.close_browser()


@pytest.fixture
def sign_in(open_browser, login_page):
    login_page.sign_in(USER_EMAIL, USER_PASSWORD)


@pytest.fixture
def open_contact_us_page(contact_us_page):
    contact_us_page.navigate()


@pytest.fixture
def open_faq_page(faq_page):
    faq_page.navigate()


@pytest.fixture
def open_homepage(homepage):
    homepage.navigate()
