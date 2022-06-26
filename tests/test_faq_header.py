import allure
import pytest

from src.page_elements.faq_page_elements import FAQPageElements
from src.wd import be


@allure.story('WIX site')
@allure.title('Test FAQ Header content')
@pytest.mark.functional
@pytest.mark.usefixtures('sign_in', 'on_fail', 'open_faq_page')
def test_faq_header():
    faq_page_elements = FAQPageElements()

    with allure.step('#1 Verify FAQ Header content'):
        faq_page_elements.help_center_header \
            .should(be.visible())
