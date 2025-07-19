from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'


@given('Open target.com')
def open_main(context):
    context.driver.get('https://www.target.com/')
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@data-test='@web/CartLink']"))
    )

@when ('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()

@then('Verify Your cart is empty message is shown')
def verify_message_empty(context):
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Your cart is empty')]").text
    expected_result = 'Your cart is empty'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'



# @given('Open target.com')
# def open_main_first(context):
#     context.driver.get("https://www.target.com/")

@when('Click Sign In')
def click_account_main(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_side(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()

@then('Verify Sign In form opened')
def verify_heading(context):
    wait = WebDriverWait(context.driver, 6)
    heading_text = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[text()='Sign in or create account']"))).text
    sleep(2)
    assert heading_text == 'Sign in or create account', f"Expected heading not found, got: {heading_text}"