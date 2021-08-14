from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    baseUrl = "http://magento-demo.lexiconn.com"
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)

    def navigate(self,addUrl) -> 'BasePage':
        url = "/".join([self.baseUrl, addUrl])
        self.driver.get(url)
        return self
    
    def tear(self):
        self.driver.close()
        self.driver.quit()
    
