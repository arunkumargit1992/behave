from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 


@step('I navigate to the facebook Home page')
def step_impl(context):
    context.browser.get("https://www.facebook.com/")
    time.sleep(2)
    
    
     
@step('I enter username password and click login button')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("behavetest10@gmail.com")    
    time.sleep(2)
    context.browser.find_element(By.ID, "pass").send_keys("behave123!@#")
    time.sleep(2)
    context.browser.find_element(By.ID, "u_0_2").click()
    time.sleep(2)
    
@step('I see my facebook home page')
def step_impl(context):
    assert_true(context.browser.find_element(By.ID, "js_1"))