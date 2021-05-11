from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import pytest

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)

        checkout_page = homepage.shop_items() # Smart way of optimizing as this will return an object of CheckoutPage Class

        products = checkout_page.get_product_titles()

        confirmpage = ConfirmPage(self.driver)

        for product in products:
            name = product.find_element_by_xpath("div/div/h4/a").text
            print(name)
            if name == "iphone X":
                product.find_element_by_xpath("div/div/button").click()

        # Clicking Checkout button
        checkout_page.checkout().click()

        selected_product = confirmpage.select_product().text

        assert selected_product == "iphone X"

        confirmpage.success().click()

        confirmpage.country().send_keys("ind")

        wait = WebDriverWait(self.driver, 7)

        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element_by_link_text("India").click()

        checkbox = self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
        checkbox.click()
        # assert checkbox.is_selected()

        self.driver.find_element_by_xpath("//input[@value='Purchase']").click()

        var = self.driver.find_element_by_class_name("alert-success")
        end_text = var.text

        print(end_text)
        assert "Success" in end_text

        self.driver.save_screenshot("screen.png")

        ##Chnages Made
