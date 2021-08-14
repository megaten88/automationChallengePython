from selenium import webdriver


class BasePage():
    baseUrl = "http://magento-demo.lexiconn.com"

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.pageUrl=""
        self.pageTitle="Madison Island"
        

    def navigate(self) -> 'BasePage':
        url = "/".join([self.baseUrl, self.pageUrl])
        self.driver.get(url)
        return self

    def getFullUrl(self):
        url = "/".join([self.baseUrl, self.pageUrl])
        return url
        
    def getDriverTitle(self):
        return self.driver.title

    def getPageTitle(self):
        return self.pageTitle
