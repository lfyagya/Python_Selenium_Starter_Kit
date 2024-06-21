import pytest
from Pages.login_page import LoginPage
from Config.config import Config

@pytest.mark.usefixtures("init_driver")
class TestLogin:

    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        self.driver.get(Config.URL)
        login_page.enter_emailid(Config.EMAILID)
        login_page.click_login_button()
        
        # Assertion to verify the login was successful
        title_message = login_page.get_title()
        assert title_message == "Automation Demo Site"
