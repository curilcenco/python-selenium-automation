from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()


driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
wait = WebDriverWait(driver, 10)
email_input = wait.until(EC.presence_of_element_located((By.ID, "ap_email")))

email_input.send_keys("i.curilcenco@gmail.ru")
continue_button = driver.find_element(By.ID, "continue").click()

driver.find_element(By.XPATH,"//input[contains(@aria-labelledby, 'continue-announce')]").click()
driver.find_element(By.XPATH,"//*[contains(@aria-labelledby, 'intention-submit-button-announce')]").click()

driver.find_element(By.ID,"twotabsearchtextbox")
driver.find_element(By.XPATH,"//a[contains(@aria-label, 'amazon.com')]")
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
driver.find_element(By.ID,"ra-sign-in-link")
driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-none.moa-country-picker-select-container")
driver.find_element(By.ID,"ap_customer_name" )
driver.find_element(By.ID,"ap_password")
driver.find_element(By.XPATH,"//*[contains(text(), 'Passwords must be at least 6 characters')]")
driver.find_element(By.ID,"ap_password_check")
driver.find_element(By.ID,"continue")
driver.find_element(By.XPATH,"//*[contains(text(), 'Buying for work?')]")
driver.find_element(By.ID,"ab-enhanced-registration-link")
driver.find_element(By.XPATH,"//*[text()='Conditions of Use']")
driver.find_element(By.XPATH,"//*[text()='Privacy Notice']")