from pages.urls import URL
from tests.base_test import BaseTest
import requests


def _test_urls(urls, appendix=''):
    broken_url = []
    for url in urls:
        url = appendix + url
        response = requests.get(url)
        if response.status_code != 200:
            broken_url.append(urls)
    return broken_url


class TestUrls(BaseTest):

    def test_external_urls(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.page = URL(self.driver)
            self.logger.info('Test External URls')
            self.logger.info('Verifying URLS')
            urls = self.page.get_external_urls()
            broken_url = _test_urls(urls)
            if len(broken_url) > 0:
                self.driver.save_screenshot(".//Screenshots//test_external_urls.png")
                self.logger.info('External URls test is failed')
                for url in broken_url:
                    self.logger.info("External url: %s is broke", url)
            else:
                self.logger.info('External URls test is passed')

            assert len(broken_url) == 0

        except:
            self.logger.info("browser crash during testing")
        finally:
            self.driver.close()

    def test_internal_urls(self, setup):
        try:
            self.driver = setup
            self.page = URL(self.driver)
            self.logger.info('Test Internal URls')
            self.logger.info('Verifying URLS')
            urls = self.page.get_external_urls()
            broken_url = _test_urls(urls, self.baseURL)
            if len(broken_url):
                self.driver.save_screenshot(".//Screenshots//test_internal_urls.png")
                self.logger.info('Internal URls test is failed')
                for url in broken_url:
                    self.logger.info("Internal url: %s is broke", url)
            else:
                self.logger.info('Internal URls test is passed')

            self.driver.close()
            assert len(broken_url) == 0

        except:
            self.logger.info("browser crash during testing")
        finally:
            self.driver.close()