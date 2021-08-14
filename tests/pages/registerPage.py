from pages.basePage import BasePage
from pages.locators import Locators
from selenium.webdriver.common.by import By
from faker import Faker
import json

class RegisterPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.pageUrl="customer/account/create"
        self.pageTitle="Create New Customer Account"

