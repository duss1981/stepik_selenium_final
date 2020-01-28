from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):        
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login from is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Register from is not presented"
        
    def register_new_user(self, email, password):
        self.browser.delete_all_cookies()
        input1 = self.browser.find_element(*LoginPageLocators.USER_EMAIL)
        input1.send_keys(str(email)) 
        input2 = self.browser.find_element(*LoginPageLocators.USER_PASS1)
        input2.send_keys(str(password))
        input3 = self.browser.find_element(*LoginPageLocators.USER_PASS2)
        input3.send_keys(str(password))
        button=self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_USER)
        button.click()
        