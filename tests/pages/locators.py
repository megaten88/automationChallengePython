#Class for challenge locators

class Locators():
    #BasePage Locators
    searchBar = "search"
    searchButton = ".button.search-button"
    def selectProduct(product:str):
        return f'//li//a[@title="{product.strip()}"]'

    def getViewDetailsButton(href:str):
        return f'//li//a[@class="button" and @href="{href.strip()}"]'

    productsGrid = "ul.products-grid"
    products = '//ul[contains(@class,"products-grid")]/li'


    #Homepage Locators
    accountDrop = '.skip-account'
    register='//a[@title="Register"]'
    login='//a[@title="Log In"]'

    #Register Locators
    firstNameInput='firstname'
    lastNameInput='lastname'
    emailInput='email_address'
    passwordInput='password'
    confirmPasswordInput='confirmation'
    submitButton='//button[@title="Register"]'

    #Login Page
    loginEmailInput = "email"
    loginPasswordInput = "pass"
    submitLogin='send2'

    #Account Info Locators
    contactInfoTitle='//h3[text()="Contact Information"]'

    def getLocatorBoxName(name,lastname):
        return f'//div[@class="box-content"]/p[contains(text(),"{name} {lastname}")]'


        