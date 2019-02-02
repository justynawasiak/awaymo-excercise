import pytest
from selenium import webdriver


@pytest.fixture
def get_driver(request):
    """
    Fixture to initiate and close the driver.
    """
    driver = webdriver.Chrome('driver/chromedriver.exe')
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.close()
