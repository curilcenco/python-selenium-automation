from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page



class SideMenu(Page):

    SIGN_IN = (By.ID, 'account-sign-in')
    LOG_IN_SIDE_NAV_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')


    def click_sign_account(self):
        self.driver.find_element(*self.SIGN_IN).click()

    def wait_and_click_b(self, *LOG_IN_SIDE_NAV_BTN):
        self.wait.until(
            EC.element_to_be_clickable(LOG_IN_SIDE_NAV_BTN),
            message=f'Element by {LOG_IN_SIDE_NAV_BTN} not clickable'
        ).click()

    def click_sign_in_side(self):
        self.driver.find_element(*self.LOG_IN_SIDE_NAV_BTN).click()

    def verify_side_partial_url(self, url):
        self.wait.until(EC.url_contains(url), message=f'URL does not contain {url}')