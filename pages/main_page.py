from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    SIGN_IN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    INSERT_EMAIL = (By.ID, 'username')
    INSERT_PASSWORD = (By.ID, 'password')
    CONTINUE_BUTTON = (By.ID, 'login')
    PASSPORT_INCORRECT_MSG = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')

    def open_main_page(self):
        self.open_url(self.base_url)
        self.wait_until_clickable(*self.SEARCH_FIELD)

    def click_account(self):
        self.find_element(*self.ACCOUNT_BUTTON).click()

    def click_sign_in(self):
        self.find_element(*self.SIGN_IN).click()

    def input_email(self, *email):
        self.find_element(*self.INSERT_EMAIL).send_keys('<gizmothegremlin@shiptudo.com>')


    def input_password(self, password):
        print("Password insert", password)
        self.find_element(*self.INSERT_PASSWORD).send_keys(password)

    def continue_button(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    def send_text(self, locator, text):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    # def verify_passport_incorrect_msg(self, expected_msg):
    #     actual_msg = self.find_element(*self.PASSPORT_INCORRECT_MSG).text
    #     assert expected_msg.lower() in actual_msg.lower(),f'Expected "{expected_msg}" not found in actual "{actual_msg}"'

    def verify_passport_incorrect_msg(self, expected_msg):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSPORT_INCORRECT_MSG))
        actual_msg = element.text
        assert expected_msg in actual_msg, f'Expected "{expected_msg}", got "{actual_msg}"'


    def wait_until_visible_(self, by, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
        )


