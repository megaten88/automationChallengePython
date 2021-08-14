from _pytest.fixtures import fixture
from pages.homePage import HomePage
import pytest
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then

scenarios("../features/challenge.feature", example_converters=dict(product=str))

@pytest.fixture()
def browser():
    browser_ = webdriver.Chrome()
    browser_.implicitly_wait(10)
    browser_.maximize_window()
    yield browser_
    browser_.quit()

@given("The automation challenge homepage")
def initTest(browser):
    HomePage(browser).navigate()