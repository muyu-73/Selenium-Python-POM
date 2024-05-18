from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, wait_time=10):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, wait_time)

