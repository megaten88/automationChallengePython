from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    baseUrl = "http://magento-demo.lexiconn.com"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.pageUrl=""
        self.pageTitle="Madison Island"

    def navigate(self) -> 'BasePage':
        url = "/".join([self.baseUrl, self.pageUrl])
        self.driver.get(url)
        return self
    
    def getDriverTitle(self):
        return self.driver.title

    def getPageTitle(self):
        return self.pageTitle
