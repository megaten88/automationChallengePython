from pytest_bdd.types import THEN
from pages.registerPage import RegisterPage
from _pytest.fixtures import fixture
from pages.homePage import HomePage
import pytest
from selenium import webdriver
from faker import Faker
from pytest_bdd import scenarios, given, when, then
import json

scenarios("../features/challenge.feature", example_converters=dict(product=str))

fake = Faker(['en_US', 'pt_BR', 'fr_FR', 'de_DE'])

@fixture()
def browser():
    browser_ = webdriver.Chrome()
    browser_.implicitly_wait(10)
    browser_.maximize_window()
    yield browser_
    browser_.quit()

#Given Steps

@given("The automation challenge homepage")
def initTest(browser):
    homePage = HomePage(browser)
    homePage.navigate()
    assert(homePage.getDriverTitle == homePage.getPageTitle)

#When Steps
@when("User creates a user Account")
def createUser(browser):
    createUser = {"firstname": fake.first_name(), "lastname": fake.last_name(), "email": fake.email(domain="yopmail.com"), "password": "Tester123!"}
    homePage = HomePage(browser)
    homePage.clickAccount()
    homePage.clickRegister()
    registerPage = RegisterPage(browser)
    assert(registerPage.getDriverTitle == registerPage.getPageTitle)
    registerPage.setFirstName(createUser["firstname"])
    registerPage.setLastName(createUser["lastname"])
    registerPage.setEmail(createUser["email"])
    registerPage.setPassword(createUser["password"])
    registerPage.setConfirmPassword(createUser["password"])
    with(open, '../userData.txt', 'w+') as datafile:
        json.dump(createUser, datafile)
    registerPage.clickSubmit()


#Then Steps
@then("User should see their data on Contact Information section")
def checkInfo(browser):
    
    pass