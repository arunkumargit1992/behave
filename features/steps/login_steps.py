from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time 


@step('I navigate to the facebook Home page')
def step_impl(context):
    context.browser.get("https://www.facebook.com/") 
    time.sleep(5)   
	  
@step('I enter username password and click login button')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("behavetest10@gmail.com")    
    context.browser.find_element(By.ID, "pass").send_keys("behave123!@#")
    context.browser.find_element(By.ID, "u_0_2").click()
    
@step('I see my facebook home page')
def step_impl(context):
    assert_true(context.browser.find_element(By.XPATH, '//*[@id="u_s_2"]/input[2]'))