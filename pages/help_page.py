from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from pages.base_page import Page


class HelpPage(Page):
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")
    TYPE_HEAD_INPUT = (By.CSS_SELECTOR, '[data-test="@web/TypeaheadInput/Input"]')
    SEARCH_BUTTON = (By.XPATH, '//div[contains(@class, "BaseButton")]')
    DROPDOWN_HELP = (By.CSS_SELECTOR, "input[data-test='@web/TypeaheadInput/Input']")
    DROPDOWN_HELP_CLICK = (By.CSS_SELECTOR, "[class*='styles_listItemLink']")



    # Dynamic locator => generates locator during the test run
    def _get_header_locator(self, header):
        # HEADER (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header)]

    def open_help_page(self):
        self.open_url ('https://www.target.com/help')


    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

     # def click_and_input(self, query: str):
     #    self.click(self.TYPE_HEAD_INPUT)
     #    self.send_text(self.TYPE_HEAD_INPUT, query)


    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def click_dropdown_help_element(self):
        self.click(*self.DROPDOWN_HELP_CLICK)


    def select_topic(self, option_value):
        dd = self.find_element(*self.TOPIC_SELECTION_DD)

        select = Select(dd)
        select.select_by_value(option_value)

    def verify_correct_help_page_opened(self, header):
        # header = Returns / Current promotions / ....
        locator = self._get_header_locator(header)
        print(locator)
        self.wait_until_visible(*locator)

    def  find_field(self):
        return self.driver.find_element(*self.DROPDOWN_HELP)

    # def verify_promotions_opened(self):
    #     self.wait_until_visible(*self.HEADER_PROMOTIONS)
    #
    # def verify_returns_opened(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)
    # def verify_dropdown_help(self, *locator):
    #     locator = self.find_element(*self.DROPDOWN_HELP)
    #     self.wait_until_visible(*DROPDOWN_HELP)
    #     print("Dropdown Verified")


    def verify_dropdown_help(self):
        print(f'DROPDOWN_HELP: {self.DROPDOWN_HELP}')
        self.wait_until_visible(*self.DROPDOWN_HELP)
        print('Appear')

    def verify_partial_url_help (self, expected_partial_url):
        # current_url = self.driver.current_url
        # print(f'Current url {current_url}')
        # assert expected_partial_url in current_url, f'Expected text {expected_partial_url} not in {current_url}'
        self.wait.until(EC.url_contains(expected_partial_url), message=f'URL does not contain {expected_partial_url}')


    def send_text_dropdown(self, text):
        element = self.driver.find_element(*self.DROPDOWN_HELP)
        element.click()
        element.clear()
        element.send_keys(text)