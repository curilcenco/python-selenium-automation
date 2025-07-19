from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_account_sign_in(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "account-sign-in")))

    def find_account_nav_sign_in(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-test='accountNav-signIn']")))

    def find_sign_in_text(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Sign in or create account')]")))

    def find_passkey_button(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Sign in with passkey')]")))


