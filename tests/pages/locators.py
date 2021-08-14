#Class for challenge locators

class Locators():
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

    #Account Info Locators
    contactInfoTitle='//h3[text()="Contact Information"]'

    def getLocatorBoxName(name,lastname):
        return f'//div[@class="box-content"]/p[contains(text(),"{name} {lastname}")]'
        