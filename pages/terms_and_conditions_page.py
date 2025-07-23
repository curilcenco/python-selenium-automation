from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import Page


class TermsAndConditions(Page):
    TC_BTT = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')

    def terms_conditions_element(self):
        return self.driver.find_element(*self.TC_BTT)

    def terms_conditions_click(self):
        self.driver.find_element(*self.TC_BTT).click()

    def switch_to(self, window_handle):
        self.driver.switch_to.window(window_handle)

    # def tc_wait_s_click(self, TC_BTT):
    #     self.wait.until(
    #         EC.element_to_be_clickable(TC_BTT),
    #         message=f'Element by {TC_BTT} not clickable' ).click()

    def verify_tc_opened(self):
        current_url = self.driver.current_url
        expected_substring = 'terms-conditions'
        assert expected_substring in current_url, f'Expected "{expected_substring}" to be in "{current_url}"'

    def verify_partial_url_tc(self, expected_substring):
        current_url = self.driver.current_url
        assert expected_substring in current_url, (
            f'Expected "{expected_substring}" to be in URL: "{current_url}"'
        )

    def verify_tc_window_closed(self):
        current_url = self.driver.current_url
        assert 'terms-conditions' not in current_url, f"'terms-conditions' still present in URL: {current_url}"

    def close_tab_and_switch(self):
        self.wait.until(EC.new_window_is_opened)
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        self.driver.close()

        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break