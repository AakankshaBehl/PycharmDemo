import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def selectOptionByText(self, locator, text):
        a = Select(locator)
        a.select_by_visible_text(text)

