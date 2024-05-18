import time

from pages.jump_buttons import JumpButtons
from tests.base_test import BaseTest


class TestJumpButton(BaseTest):

    def test_jump_buttons(self, setup):
        try:
            self.driver = setup
            self.driver.get(self.baseURL)
            self.page = JumpButtons(self.driver)
            self.logger.info('Test Jumps Buttons')
            self.logger.info('Waiting for buttons loads')
            scroll_position = self.driver.execute_script("return window.pageYOffset;")
            jump_buttons = self.page.get_jump_buttons()
            broke_buttons = []
            self.logger.info('Waiting for jump buttons')
            for jump_button in jump_buttons:
                self.logger.info(jump_button)
                location_id = str(jump_button.get_attribute('href')).split('#')[1]
                self.logger.info(location_id)
                jump_button.click()
                #time.sleep(1) #for visualization
                display = self.page.is_visible(location_id)
                #time.sleep(1) #for visualization
                if not display:
                    broke_buttons.append(location_id)
                self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")

            if len(broke_buttons) > 0:
                for broke_button in broke_buttons:
                    self.logger.info("%s is not working", broke_button)

            assert len(broke_buttons) == 0

        finally:
            self.driver.close()