import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


# Get browser type from cli/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        'Project Name': 'TVO',
        'Module Name': 'Grade 8 Math',
        'Tester': 'Xuen'
    }


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
