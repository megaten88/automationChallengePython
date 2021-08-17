import pytest
from pages.registerPage import RegisterPage
from pages.homePage import HomePage
from pages.accountInfoPage import AccountInfoPage
from pages.loginPage import LoginPage
from faker import Faker
from pytest_bdd import given, when, then
import json
import re


fake = Faker(['en_US', 'pt_BR', 'fr_FR', 'de_DE'])


#Given Steps

@given("The automation challenge homepage")
def initTest(browser):
    homePage = HomePage(browser)
    homePage.navigate()
    assert(homePage.getDriverTitle() == homePage.getPageTitle())

@given("An existing user")
def loginUser(browser):
    user = None 
    try:
        with open("userData.json") as datafile:
            user = json.load(datafile)
    except:
        print("No userData.json found")
        pytest.exit("No userData.json found")
    assert(user["firstname"] !=None )
    assert(user["lastname"] !=None )
    assert(user["email"]!=None )
    homePage = HomePage(browser)
    homePage.clickAccount()
    homePage.clickLogin()
    loginPage = LoginPage(browser)
    assert(loginPage.getDriverTitle() == loginPage.getPageTitle())
    assert(loginPage.driver.current_url == loginPage.getFullUrl())
    loginPage.setEmail(user["email"])
    loginPage.setPassword(user["password"])
    loginPage.clickSubmit()
    assert(loginPage.driver.current_url == "http://magento-demo.lexiconn.com/customer/account/")

#When Steps
@when("User creates a user Account")
def createUser(browser):
    createUser = {"firstname": fake.first_name(), "lastname": fake.last_name(), "email": fake.email(domain="yopmail.com"), "password": "Tester123!"}
    homePage = HomePage(browser)
    homePage.clickAccount()
    homePage.clickRegister()
    registerPage = RegisterPage(browser)
    assert(registerPage.getDriverTitle() == registerPage.getPageTitle())
    assert(registerPage.driver.current_url == registerPage.getFullUrl())
    # Insert User Data
    registerPage.setFirstName(createUser["firstname"])
    registerPage.setLastName(createUser["lastname"])
    registerPage.setEmail(createUser["email"])
    registerPage.setPassword(createUser["password"])
    registerPage.setConfirmPassword(createUser["password"])

    # Save User Data for Next Scenario and Steps
    try:
        with open('userData.json', 'w+') as datafile:
            json.dump(createUser, datafile)
        datafile.close()
    except:
        pytest.exit("Could not write into userData.json")
        
    registerPage.clickSubmit()

@when('The user searches for a desired product <product>')
def searchProduct(browser,product:str):
    #Start from logged user page
    loggedUserPage = AccountInfoPage(browser)
    assert(loggedUserPage.getDriverTitle() == loggedUserPage.getPageTitle())
    loggedUserPage.search(product)
    assert(loggedUserPage.getProductsLen()>0)

@when('Goes into the <product> details page')
def viewDetails(browser,product:str):
    loggedUserPage = AccountInfoPage(browser)
    loggedUserPage.getProduct(product)
    desiredProduct = loggedUserPage.getProductUrl()
    loggedUserPage.viewDetails()
    assert(loggedUserPage.driver.current_url == desiredProduct)

    

#Then Steps
@then("User should see their data on Contact Information section")
def checkInfo(browser):
    accountInfo = AccountInfoPage(browser)
    assert(accountInfo.getDriverTitle() == accountInfo.getPageTitle())
    assert(accountInfo.driver.current_url == accountInfo.getFullUrl())
    assert(accountInfo.getContactInfo().text == "CONTACT INFORMATION")
    data = None
    #Load User Data
    try:
        with open("userData.json") as datafile:
            data = json.load(datafile)
    except:
        print("No userData.json found")
        pytest.exit("No userData.json found")
    
    accountInfo.getPersonalBox(data["firstname"], data["lastname"])
    results = re.search("([\w ]*)\\n([\w\d.-@]*)\\nChange Password", accountInfo.getText())
    # Compare User Data
    assert results[1] == f"{data['firstname']} {data['lastname']}" 
    assert results[2] == data["email"]

@then('The user should be in correct <product> detail page')
def checkDetails(browser,product:str):
    loggedUserPage = AccountInfoPage(browser)
    assert(loggedUserPage.getDriverTitle() == product.strip())

