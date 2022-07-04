import allure
import pytest

from src.models.contact_us_model import ContactUsModel


@allure.story('WIX site')
@allure.title('Test Contact US Submit form')
@pytest.mark.functional
@pytest.mark.usefixtures('sign_in', 'on_fail')
def test_contact_us_submit_form(contact_us_page, open_contact_us_page, human_verification_modal):
    contact_us_model = ContactUsModel.create()

    with allure.step('#1 Fill in "Submit Form" with valid parameters ->'
                     'Verify "Submit Form" content'):
        contact_us_page \
            .submit_contact_us_form(contact_us_model) \
            .verify_contact_us_form_content(contact_us_model)

    with allure.step('#2 Click "Submit" button'):
        # TODO expected to fail here
        contact_us_page \
            .click_submit_button()

    with allure.step('#3 Check if "Human Verification" modal is present'):
        human_verification_modal \
            .verify_presence_of_modal(is_present=True)
