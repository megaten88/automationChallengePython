from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expc
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver) 

    def getAccountSelect(self) -> WebElement:
        self.accountSelect = self.driver.find_element(By.CSS_SELECTOR, Locators.accountDrop)
        return self.accountSelect
    
    def getRegisterOption(self) -> WebElement:
        self.registerOption = self.driver.find_element(By.XPATH, Locators.register)
        return self.registerOption
    
    def getLogInOption(self) -> WebElement:
        self.logInOption = self.driver.find_element(By.XPATH, Locators.login)
        return self.logInOption

    def clickAccount(self):
        accountButton: WebElement = self.wait.until(expc.element_to_be_clickable((By.CSS_SELECTOR,Locators.accountDrop)))
        accountButton.click()

    def clickRegister(self):
        register: WebElement = self.wait.until(expc.element_to_be_clickable((By.XPATH,Locators.register)))
        register.click()

    def clickLogin(self):
        login: WebElement = self.wait.until(expc.element_to_be_clickable((By.XPATH,Locators.login)))
        login.click()

