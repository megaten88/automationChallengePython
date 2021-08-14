from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expc

class RegisterPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.pageUrl="customer/account/create"
        self.pageTitle="Create New Customer Account"
    
    # Getters in case needed
    def getFirstNameInput(self) -> WebElement:
        self.firstName = self.driver.find_element(By.ID,Locators.firstNameInput)
        return self.firstName

    def getLastNameInput(self)-> WebElement:
        self.lastName = self.driver.find_element(By.ID,Locators.lastNameInput)
        return self.lastName
    
    def getEmailInput(self)-> WebElement:
        self.emailInput = self.driver.find_element(By.ID,Locators.emailInput)
        return self.emailInput
    
    def getPasswordInput(self) -> WebElement:
        self.passwordInput = self.driver.find_element(By.ID,Locators.passwordInput)
        return self.passwordInput

    def getConfirmInput(self)-> WebElement:
        self.confirmInput = self.driver.find_element(By.ID,Locators.confirmPasswordInput)
        return self.confirmInput

    def getSubmitButton(self)-> WebElement:
        self.submitButton =  self.driver.find_element(By.XPATH, Locators.submitButton)
        return self.submitButton

    def setFirstName(self, firstname):
        self.getFirstNameInput().send_keys(firstname)
    
    def setLastName(self, lastname):
        self.getLastNameInput().send_keys(lastname)

    def setEmail(self, email):
        self.getEmailInput().send_keys(email)
    
    def setPassword(self, password):
        self.getPasswordInput().send_keys(password)

    def setConfirmPassword(self,password):
        self.getConfirmInput().send_keys(password)

    def clickSubmit(self):
        self.getSubmitButton().click()
        WebDriverWait(self.driver, 10).until(expc.url_changes(self.getFullUrl()))

