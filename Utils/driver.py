from selenium import webdriver

class WebDriverManager:

    def get_driver(self):
        driver = webdriver.Chrome()  # You can customize this to fetch from config or use other drivers
        driver.maximize_window()
        return driver

