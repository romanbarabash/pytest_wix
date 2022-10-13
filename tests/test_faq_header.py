import allure
import pytest

from src.page_elements.faq_page_elements import FAQPageElements
from src.webdriver import be


@allure.story('WIX site')
@allure.title('Test FAQ Header content')
@pytest.mark.functional
@pytest.mark.usefixtures('sign_in', 'on_fail')
def test_faq_header(open_faq_page):
    faq_page_elements = FAQPageElements()

    with allure.step('#1 Verify FAQ Header content'):
        faq_page_elements.help_center_header \
            .should(be.visible())
