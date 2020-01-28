from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    
    def should_not_be_success_message(self):        
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
        "Something in basket is presented, but should not be"
        
        
    def should_be_empty_basket_message(self):        
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY),\
        "Something in basket is presented, but should be empty"
        
        
    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_FORM), \
        "Something in basket is dissappeared, but should not be"        
        #time.sleep(10)    
        
    