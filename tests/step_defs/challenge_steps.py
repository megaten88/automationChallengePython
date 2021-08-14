import pytest
from pytest_bdd.types import THEN
from pages.registerPage import RegisterPage
from pages.homePage import HomePage
from faker import Faker
from pytest_bdd import given, when, then
import json


fake = Faker(['en_US', 'pt_BR', 'fr_FR', 'de_DE'])


#Given Steps

@given("The automation challenge homepage")
def initTest(browser):
    homePage = HomePage(browser)
    homePage.navigate()
    assert(homePage.getDriverTitle() == homePage.getPageTitle())

#When Steps
@when("User creates a user Account")
def createUser(browser):
    createUser = {"firstname": fake.first_name(), "lastname": fake.last_name(), "email": fake.email(domain="yopmail.com"), "password": "Tester123!"}
    homePage = HomePage(browser)
    homePage.clickAccount()
    homePage.clickRegister()
    registerPage = RegisterPage(browser)
    assert(registerPage.getDriverTitle() == registerPage.getPageTitle())
    registerPage.setFirstName(createUser["firstname"])
    registerPage.setLastName(createUser["lastname"])
    registerPage.setEmail(createUser["email"])
    registerPage.setPassword(createUser["password"])
    registerPage.setConfirmPassword(createUser["password"])
    print(open)
    with open('userData.json', 'w+') as datafile:
        json.dump(createUser, datafile)
        datafile.close()
    registerPage.clickSubmit()
    

#Then Steps
@then("User should see their data on Contact Information section")
def checkInfo(browser):
    
    pass