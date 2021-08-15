from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expc

class LoginPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.pageUrl="customer/account/login/"
        self.pageTitle="Customer Login"
    
    # Getters in case needed
    def getEmailInput(self)-> WebElement:
        self.emailInput = self.driver.find_element(By.ID,Locators.loginEmailInput)
        return self.emailInput
    
    def getPasswordInput(self) -> WebElement:
        self.passwordInput = self.driver.find_element(By.ID,Locators.loginPasswordInput)
        return self.passwordInput

    def getSubmitButton(self)-> WebElement:
        self.submitButton =  self.driver.find_element(By.ID, Locators.submitLogin)
        return self.submitButton

    def setEmail(self, email):
        self.getEmailInput().send_keys(email)
    
    def setPassword(self, password):
        self.getPasswordInput().send_keys(password)

    def clickSubmit(self):
        self.getSubmitButton().click()
        self.wait.until(expc.url_changes(self.getFullUrl()))
        

