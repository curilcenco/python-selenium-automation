from behave import given, when, then
from time import sleep


@given('Open sign in page')
def click_sigh_in_link(context):
    context.app.main_page.open_main_page()
    sleep(3)

    # context.app.main_page.click_log_in()
    # context.app.side_menu.wait_and_click_b()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print(context.original_window)

@when('Click on Terms and Conditions link')
def click_terms_link(context):
    context.app.terms_and_conditions_page.terms_conditions_click()


@then('Close new window and switch')
def close_current_tab_and_switch(context):
    print()
    context.app.base_page.switch_to_new_window(context.driver.window_handles[1])
    sleep(7)

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_open(context):
    context.app.terms_and_conditions_page.verify_partial_url_tc('terms-conditions')

@when("Switch to the newly opened window")
def switch_opened_window(context):
    context.app.main_page.switch_to_window(context.original_window)

@then ('Verify original')
def verify_original_window(context):
    context.app.terms_and_conditions_page.base_page.verify_url('https://www.target.com/')