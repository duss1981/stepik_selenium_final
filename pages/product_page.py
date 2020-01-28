from .base_page import BasePage
from .locators import ProductPageLocators
#import time

class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.delete_all_cookies()
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        
        
    def get_data_product(self):    
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        
    
    def should_be_correct_product_name(self):
        basket_product = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_SUCCESS_MESSAGE).text        
        assert self.product_name==basket_product, \
        f"Product name is not similar '{self.product_name}' != '{basket_product}'" 
    
    
    def should_not_be_product_name_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_PRODUCT_SUCCESS_MESSAGE), \
        f"Product is in basket {self.product_name}, but should not be" 
        
    
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE),\
        f"Product is in basket {basket_price.text}, but should not be" 
        
        
    def should_be_correct_product_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text        
        assert self.product_price==basket_price, \
        f"Product name is not similar '{self.product_price}' != '{basket_price}'" 
        
        
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not presented, but should be"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
      
    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)==True, \
        "Success message is dissappeared, but should not be"        
        #time.sleep(10)    
    def should_be_login_page(self):
        current_url = self.browser.current_url;        
        assert '/login/' in current_url , "Admin page is not open"        
        #time.sleep(10)    