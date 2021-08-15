from _typeshed import Self
from selenium import webdriver
from pages.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expc

class BasePage():
    baseUrl = "http://magento-demo.lexiconn.com"

    def __init__(self, driver:webdriver):
        self.driver = driver
        self.pageUrl=""
        self.pageTitle="Madison Island"
        self.wait = WebDriverWait(self.driver, 10)
        

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

    def search(self, product:str):
        self.searchBar: WebElement = self.driver.find_element(By.ID,Locators.searchBar)
        self.searchButton: WebElement = self.driver.find_element(By.ID, Locators.searchButton)
        self.searchBar.send_keys(product)
        self.searchButton.click()
        self.wait.until(expc.url_changes(self.getFullUrl()))

    def getProductsLen(self) -> int: 
        self.productGrid: WebElement = self.wait.until(expc.visibility_of((By.CSS_SELECTOR,Locators.productsGrid)))
        self.products = self.driver.find_elements(By.XPATH, Locators.products)
        return len(self.products)

    def getProduct(self, product:str) -> WebElement:
        self.product = self.driver.find_element(By.XPATH, Locators.selectProduct(product))
        return self.product

    def viewDetails(self):
        self.details: WebElement = self.driver.find_element(By.XPATH, Locators.getViewDetailsButton(self.product.get_attribute("href")))
        self.details.click()
        self.wait.until(expc.url_to_be(self.product.get_attribute("href")))
        
    
