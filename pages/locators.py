from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
                  
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")    
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")    
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    USER_EMAIL =(By.CSS_SELECTOR,  '#id_registration-email')
    USER_PASS1 =(By.CSS_SELECTOR,  '#id_registration-password1')
    USER_PASS2 =(By.CSS_SELECTOR,  '#id_registration-password2')
    BUTTON_REGISTER_USER =(By.XPATH,  '//button [@name="registration_submit"]')             
                                  
class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    BASKET_PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")    
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")    
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
        
class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".basket-items")
                     
                     