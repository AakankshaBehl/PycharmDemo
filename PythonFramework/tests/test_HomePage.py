import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self,getdata):

        homepage = HomePage(self.driver)

        homepage.getname().click()
        homepage.getname().send_keys(getdata[0])
        homepage.getEmail().send_keys(getdata[1])
        homepage.getCheckBox().click()
        #a = Select(homepage.getGender())
        #a.select_by_visible_text("Male")

        self.selectOptionByText(homepage.getGender(), getdata[2])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

    @pytest.fixture(params=[("Rahul","Shetty","Male"),("Aaku","Behl","Female")])
    def getdata (self, request):
        return request.param()

