from selenium import webdriver
from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class AccountInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.pageUrl="customer/account/index/"
        self.pageTitle="My Account"

    # Getters in case needed
    def getContactInfo(self) -> WebElement :
        self.contactInfo = self.driver.find_element(By.XPATH, Locators.contactInfoTitle)
        return self.contactInfo
    
    def getPersonalBox(self,name,lastname) -> WebElement:
        self.personalBox = self.driver.find_element(By.XPATH, Locators.getLocatorBoxName(name,lastname))
        return self.personalBox

    def getText(self):
        return self.personalBox.text
    