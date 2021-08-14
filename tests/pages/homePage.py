from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.accountSelect = self.driver.find_element(By.CSS_SELECTOR, Locators.accountDrop)
        self.registerOption = self.driver.find_element(By.XPATH, Locators.register)
        self.logInOption = self.driver.find_element(By.XPATH, Locators.login)

    def getAccountSelect(self):
        return self.accountSelect
    
    def getRegisterOption(self):
        return self.registerOption
    
    def getRegisterOption(self):
        return self.logInOption
    
