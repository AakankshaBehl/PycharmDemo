from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product_title = (By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']")
    checkout_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")


    def get_product_titles(self):
        return self.driver.find_elements(*CheckoutPage.product_title)

    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

