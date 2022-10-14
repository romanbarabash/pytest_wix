from src.elements_manager import element, by


class ContactUsPageElements:
    def __init__(self):
        # region contact us form elements
        self.name_field = element(by.xpath("//*[@placeholder='Enter your name']"))
        self.address_field = element(by.xpath("//*[@placeholder='Enter your address']"))
        self.email_field = element(by.xpath("//*[@placeholder='Enter your email']"))
        self.phone_field = element(by.xpath("//*[@placeholder='Enter your phone number']"))
        self.subject_field = element(by.xpath("//*[@placeholder='Type the subject']"))
        self.message_textarea = element(by.xpath("//textarea[contains(@id,'textarea')]"))
        # endregion

        self.submit_button = element(by.xpath("//!!!button[./*[text()='Submit']]"))
