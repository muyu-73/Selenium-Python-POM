from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


def get_location_id(jump_button):
    return str(jump_button.get_attribute('href')).split('#')[1]


class JumpButtons(BasePage):
    jump_button_class_name = "button-small"

    def wait_jump_button(self):
        self._wait.until(ec.element_to_be_clickable((By.CLASS_NAME, self.jump_button_class_name)))

    def get_jump_buttons(self):
        jump_buttons = self._driver.find_elements(By.CLASS_NAME, self.jump_button_class_name)
        return jump_buttons

    def is_visible(self, button_id):
        ele = self._driver.find_elements(By.ID, button_id)
        if len(ele) != 0:
            return ele[0].is_displayed()

        return False


