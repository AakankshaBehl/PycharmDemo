from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:
        def __init__(self,driver):
            self.driver= driver


        shop = (By.CSS_SELECTOR, "a[href*='shop']")
        name = (By.NAME, "name")
        email = (By.NAME, "email")
        pwd = (By.XPATH, "//input[@type='password']")
        check = (By.ID, "exampleCheck1")
        gender = (By.ID, "exampleFormControlSelect1")
        submit = (By.XPATH, "//input[@value='Submit']")
        successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")


        def shop_items(self):
            self. driver.find_element(*HomePage.shop).click() # Star reads it as a tuple
            checkoutpage = CheckoutPage(self.driver)
            return checkoutpage

        def getname(self):
            return self.driver.find_element(*HomePage.name)

        def getEmail(self):
            return self.driver.find_element(*HomePage.email)

        def getCheckBox(self):
            return self.driver.find_element(*HomePage.check)

        def getGender(self):
            return self.driver.find_element(*HomePage.gender)

        def submitForm(self):
            return self.driver.find_element(*HomePage.submit)

        def getSuccessMessage(self):
            return self.driver.find_element(*HomePage.successMessage)
