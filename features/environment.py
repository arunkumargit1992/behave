from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome("E://chromedriver.exe")
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    context.browser.set_page_load_timeout(50)
    context.browser.implicitly_wait(30)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
