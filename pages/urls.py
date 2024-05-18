from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class URL(BasePage):
    url_tag_name = "a"

    def get_urls(self):
        link_elements = self._driver.find_elements(By.TAG_NAME, self.url_tag_name)
        urls = map(lambda url: url.get_attribute("href"), link_elements)
        return urls

    def get_external_urls(self):
        links = self.get_urls()
        return [link for link in links if not str(link).startswith("/")]

    def get_internal_urls(self):
        links = self.get_urls()
        return [link for link in links if str(link).startswith("/")]
