import allure

from src.exception_handler import retry
from src.models.contact_us_model import ContactUsModel
from src.page_elements.contact_us_page_elements import ContactUsPageElements
from src.page_objects.base_page import BasePage
from src.wd import have


class ContactUsPage(BasePage):
    PATH = 'contact'

    def __init__(self):
        super().__init__()

        self.contact_us_page_elements = ContactUsPageElements()

    def submit_contact_us_form(self, contact_us: ContactUsModel):
        with allure.step('Fill "Contact us" form'):
            allure.attach(contact_us.to_json(), 'Test Data', allure.attachment_type.TEXT)
            self.contact_us_page_elements.name_field.send_keys(contact_us.name)
            self.contact_us_page_elements.address_field.send_keys(contact_us.address)
            self.contact_us_page_elements.email_field.send_keys(contact_us.email)
            self.contact_us_page_elements.phone_field.send_keys(contact_us.phone)
            self.contact_us_page_elements.subject_field.send_keys(contact_us.subject)
            self.contact_us_page_elements.message_textarea.send_keys(contact_us.message)
        return self

    @retry()
    def verify_contact_us_form_content(self, contact_us: ContactUsModel):
        with allure.step('Verify "Contact us" form content'):
            allure.attach(contact_us.to_json(), 'Test Data', allure.attachment_type.TEXT)
            self.contact_us_page_elements.name_field.should(have.value(contact_us.name))
            self.contact_us_page_elements.address_field.should(have.value(contact_us.address))
            self.contact_us_page_elements.email_field.should(have.value(contact_us.email))
            self.contact_us_page_elements.phone_field.should(have.value(contact_us.phone))
            self.contact_us_page_elements.subject_field.should(have.value(contact_us.subject))
        return self

    def click_submit_button(self):
        with allure.step('Click "Submit" button'):
            self.contact_us_page_elements.submit_button.click()
        return self
