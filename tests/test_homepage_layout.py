import allure
import pytest

from src.page_elements.homepage_elements import HomepageElements
from src.wd import be



@allure.story('WIX site')
@allure.title('Test Home page layout')
@pytest.mark.functional
@pytest.mark.usefixtures('sign_in', 'on_fail', 'open_homepage')
def test_homepage_layout():
    homepage_elements = HomepageElements()

    with allure.step('#1 Verify Header content'):
        homepage_elements.celebrating_beauty_and_style_header \
            .should(be.visible())

        homepage_elements.celebrating_beauty_and_style_body \
            .should(be.visible())

    with allure.step('#2 Verify Shop now button is present'):
        homepage_elements.shop_now_button \
            .should(be.visible())
