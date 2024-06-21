import pytest
from Utils.driver import WebDriverManager

@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = WebDriverManager().get_driver()
    request.cls.driver = web_driver
    yield
    web_driver.quit()
