import pytest

from config import USER_EMAIL, USER_PASSWORD
from src.page_objects.base_page import HumanVerificationModal
from src.page_objects.contact_us_page import ContactUsPage
from src.page_objects.faq_page import FAQPage
from src.page_objects.homepage import HomePage
from src.page_objects.login_page import LoginPage
from src.wd.br import browser_options


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


# endregion pages


# region modals
@pytest.fixture(scope='session')
def human_verification_modal() -> HumanVerificationModal:
    return HumanVerificationModal()


# endregion modals


@pytest.fixture(scope='package')
def open_browser():
    browser_options.open_browser()
    yield
    browser_options.close_browser()


@pytest.fixture(scope='package')
def sign_in(open_browser):
    LoginPage().sign_in(USER_EMAIL, USER_PASSWORD)


@pytest.fixture
def open_contact_us_page(contact_us_page):
    contact_us_page.navigate()


@pytest.fixture
def open_faq_page(faq_page):
    faq_page.navigate()


@pytest.fixture
def open_homepage(homepage):
    homepage.navigate()
