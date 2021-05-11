from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    selected_product = (By.LINK_TEXT, "iphone X")
    success_button = (By.CSS_SELECTOR, "button[class*='btn btn-success']")
    country_field = (By.ID, "country")




    def select_product(self):
        return self.driver.find_element(*ConfirmPage.selected_product)

    def success(self):
        return self.driver.find_element(*ConfirmPage.success_button)

    def country(self):
        return self.driver.find_element(*ConfirmPage.country_field)

