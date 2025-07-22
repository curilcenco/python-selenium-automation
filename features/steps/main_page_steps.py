from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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


@given('Open target')
def open_cart(context):
    context.driver.get('https://www.target.com/')

@when('Click Sign In')
def click_sign_in(context):
    context.app.side_menu_page.click_sign_account()

@when('Side navigation menu')
def side_navigation_menu_click(context):
    context.app.side_menu_page.click_sign_in_side()

@then('Verify Sign In')
def verify_sign_in(context):
    context.app.side_menu_page.verify_side_partial_url("login")