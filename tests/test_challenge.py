from step_defs.challenge_steps import *
from selenium import webdriver
from _pytest.fixtures import fixture
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenarios

scenarios("features/challenge.feature", example_converters=dict(product=str))

@fixture()
def browser():
    browser_ = webdriver.Chrome(ChromeDriverManager().install())
    browser_.implicitly_wait(10)
    browser_.maximize_window()
    browser_.set_page_load_timeout(30)
    yield browser_
    browser_.quit()