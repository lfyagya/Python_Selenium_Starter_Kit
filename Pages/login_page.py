from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    EMAILID_INPUT = (By.ID, "email")
    # PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.ID, 'enterimg')
    TITLE = (By.XPATH, "//h1[contains(.,'Automation Demo Site')]")

    def enter_emailid(self, emailid):
        self.send_keys(self.EMAILID_INPUT, emailid)

    # def enter_password(self, password):
    #     self.send_keys(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def get_title(self):
        return self.find_element(self.TITLE).text