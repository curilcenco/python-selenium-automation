from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")


@given('Open target main page')
def open_target_main(context):
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.header.search(search_word)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()


@then('Verify at least 1 link shown')
def verify_1_header_link_shown(context):
    link = context.driver.find_element(*HEADER_LINKS)
    print(link)
    # Stale Element Reference Ex
    # print("Before refresh:", link)
    # context.driver.refresh()
    # link = context.driver.find_element(*HEADER_LINKS)
    # link.click()
    # print("AFTER refresh:", link)


@then('Verify {link_amount} links shown')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount) # "6" => int 6
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'

@given('Open target main')
def open_main_first(context):
    context.driver.get("https://www.target.com/")

@when('Click Account')
def click_account_main(context):
    context.app.main_page.click_account()

@when('Sign in')
def click_sign_in_side(context):
    context.app.main_page.click_sign_in()

@when('Enters correct email and click Continue')
def enters_correct_email(context):
    context.app.main_page.input_email()
    sleep(2)

@when('Click Continue')
def click_continue(context):
    context.app.main_page.continue_button()


@when('Incorrect password')
def incorrect_password(context):
    context.app.main_page.input_password('1234QWerty')
    sleep(2)


@when('Clicks Sign in with password')
def clicks_sign_in_pass(context):
    context.app.main_page.continue_button()

@then('Verifies that an error message is shown')
def verify_error_message(context):
    context.app.main_page.verify_passport_incorrect_msg("incorrect")
    sleep(5)