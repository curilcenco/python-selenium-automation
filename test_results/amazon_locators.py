from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
try:
    amazon_logo = driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")
    email_field = driver.find_element(By.ID, "ap_email")
    continue_button = driver.find_element(By.ID, "continue")
    conditions_link = driver.find_element(By.XPATH, "//a[contains(@href,'condition_of_use')]")
    privacy_notice = driver.find_element(By.XPATH, "//a[contains(@href,'privacy_notice')]")
    need_help = driver.find_element(By.XPATH, "//span[contains(text(),'Need help?')]")
    forgot_password = driver.find_element(By.ID, "auth-fpp-link-bottom")
    other_issues = driver.find_element(By.ID, "ap-other-signin-issues-link")
    create_account_button = driver.find_element(By.ID, "createAccountSubmit")

    print("Amazon logo:", amazon_logo.get_attribute("href"))
    print("Email field present:", email_field.is_displayed())
    print("Continue button text:", continue_button.get_attribute("value"))
    print("Conditions of Use:", conditions_link.text)
    print("Privacy Notice:", privacy_notice.text)
    print("Need help link:", need_help.text)
    print("Forgot password link:", forgot_password.text)
    print("Other issues link:", other_issues.text)
    print("Create your Amazon account button:", create_account_button.text)

except Exception as Error:
    print("Error occurred:", Error)


