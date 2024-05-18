from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class Vocabulary(BasePage):
    vocabulary_subject_xpath = '//*[@id="s-1ad58468-2bce-457a-8653-3490182103fd"]'
    number_xpath = '//*[@id="tab-573030cc-5fb9-46ac-ad58-20ed5df58f19"]/div/span'
    algebra_xpath = '//*[@id="tab-824b1f90-66aa-48f0-8bff-b1e30d07d211"]/div[1]/span'
    data_xpath = '//*[@id="tab-b6c25143-c2a8-49b8-bbea-ace9c5dd29e8"]/div[1]/span'
    spatial_sense_xpath = '//*[@id="tab-cbbc0562-4bd1-42fd-8b09-ac9a34d6bafc"]/div/span'
    financial_literacy_xpath = '//*[@id="tab-624ed509-ef7e-4f7a-95e5-b45255c92ad8"]/div/span/font/span'
    number_content_xpath = '//*[@id="s-f1ad9c3a-424d-44b6-8741-0442bb3dcb01"]'
    algebra_content_xpath = '//*[@id="s-2b60d913-96df-4098-a4e5-6b906e646789"]'
    data_content_xpath = '//*[@id="tab-b6c25143-c2a8-49b8-bbea-ace9c5dd29e8"]/div[1]/span'
    spatial_sense_content_xpath = '//*[@id="s-8a7bf9bc-2396-4b92-a994-922b73096e29"]'
    financial_literacy_content_xpath = '//*[@id="s-6b66807d-86da-415b-a181-c1b6d608b133"]'

    contents = {'number': {'xpath': '//*[@id="tab-573030cc-5fb9-46ac-ad58-20ed5df58f19"]/div/span',
                           'content_xpath': '//*[@id="s-f1ad9c3a-424d-44b6-8741-0442bb3dcb01"]'},
                'data': {'xpath': '//*[@id="tab-b6c25143-c2a8-49b8-bbea-ace9c5dd29e8"]/div[1]/span',
                         'content_xpath': '//*[@id="tab-b6c25143-c2a8-49b8-bbea-ace9c5dd29e8"]/div[1]/span'},
                'algebra': {'xpath': '//*[@id="tab-824b1f90-66aa-48f0-8bff-b1e30d07d211"]/div[1]/span',
                            'content_xpath': '//*[@id="s-2b60d913-96df-4098-a4e5-6b906e646789"]'},
                'spatial_sense': {'xpath': '//*[@id="tab-cbbc0562-4bd1-42fd-8b09-ac9a34d6bafc"]/div/span',
                                  'content_xpath': '//*[@id="s-8a7bf9bc-2396-4b92-a994-922b73096e29"]'},
                'financial_literacy': {
                    'xpath': '//*[@id="tab-624ed509-ef7e-4f7a-95e5-b45255c92ad8"]/div/span/font/span',
                    'content_xpath': '//*[@id="s-6b66807d-86da-415b-a181-c1b6d608b133"]'},
                }

    def find_content_type(self, content_type):
        return self._driver.find_elements(By.XPATH, self.contents[content_type]['xpath'])

    def find_content(self, content_type):
        return self._driver.find_elements(By.XPATH, self.contents[content_type]['content_xpath'])

    def wait_contents(self):
        self._wait.until(ec.element_to_be_clickable((By.XPATH, self.vocabulary_subject_xpath)))

    def is_visible(self, content_xpath):
        ele = self._driver.find_elements(By.XPATH, content_xpath)
        if len(ele) != 0:
            return ele[0].is_displayed()

        return False
