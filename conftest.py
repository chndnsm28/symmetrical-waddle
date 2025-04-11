import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="selecting browser"
    )


@pytest.fixture(scope="function")
def browser_code(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
    elif browser_name == 'ie':
        driver = webdriver.Ie()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()