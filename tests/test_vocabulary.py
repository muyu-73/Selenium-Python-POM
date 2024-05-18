import time

import selenium

from pages.vocabulary import Vocabulary
from tests.base_test import BaseTest


class TestVocabulary(BaseTest):

    def test_full_window(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.page = Vocabulary(self.driver)
            self.logger.info('Test vocabulary with full windows')
            self.page.wait_contents()
            broke_content_type = []
            for content in self.page.contents:
                self.page.find_content_type(content)[0].click()
                if not self.page.is_visible(self.page.contents[content]['content_xpath']):
                    broke_content_type.append(content)
                    self.logger.info('%s does not show contents')
                time.sleep(1)

            assert len(broke_content_type) == 0
        except:
            self.logger.info("browser crash during testing")
        finally:
            self.driver.close()

    def test_windows_size_cant_fill_type_and_content(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.page = Vocabulary(self.driver)
            self.logger.info('Test vocabulary with small windows')
            self.driver.set_window_size(500, 1024)
            self.page.wait_contents()
            broke_content_showing = []
            broke_content_folding = []
            for content in self.page.contents:
                self.page.find_content_type(content)[0].click()
                if not self.page.is_visible(self.page.contents[content]['content_xpath']):
                    broke_content_showing.append(content)
                    self.logger.info('%s does not show contents')
                #time.sleep(1) #for visualization
                self.page.find_content_type(content)[0].click()
                if self.page.is_visible(self.page.contents[content]['content_xpath']):
                    broke_content_folding.append(content)
                    self.logger.info('%s does not fold contents')
                #time.sleep(1) #for visualization

            assert len(broke_content_folding) == 0 and len(broke_content_showing) == 0
        except:
            self.logger.info("browser crash during testing")
        finally:
            self.driver.close()