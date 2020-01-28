import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time

#@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()    
    page.go_to_login_page()    
    page.should_be_login_page()
    
#@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                  marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])   
                                  
                                  
def  test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.get_data_product()             
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()    
    page.should_be_correct_product_name()
    page.should_be_correct_product_price()
    
#@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'#
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()    
    page.should_not_be_product_name_in_basket()
    page.should_be_basket_empty()

   
@pytest.mark.need_review   
class TestUserAddToBasketFromProductPage():     
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"    
        page = LoginPage(browser, self.link) 
        page.open()        
        page.go_to_login_page()        
        self.email = str(time.time()) + "@fakemail.org"        
        page.register_new_user(self.email,'abcd'+ str(time.time()))        
        time.sleep(3) 
        page.should_be_authorized_user()        
        time.sleep(3)            
        
    def  test_user_can_add_product_to_basket(self, browser):#
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, self.link) 
        page.open()
        time.sleep(3)            
        page.add_item_to_basket()          

    

    

        
   