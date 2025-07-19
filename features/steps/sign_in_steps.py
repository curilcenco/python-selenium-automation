from behave import given, when, then


@given('Open Target')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when ('Check the locators')
def check_locators(context):
    context.sign_in_page.find_account_sign_in()
    context.sign_in_page.find_account_nav_sign_in()
    context.sign_in_page.find_sign_in_text()
    context.sign_in_page.find_passkey_button()

@then('Show result')
def show_result(context):
    print("Account sign-in text:", context.sign_in_page.find_account_sign_in().text)
    print("Nav sign-in text:", context.sign_in_page.find_account_nav_sign_in().text)
    print("Sign in or create account:", context.sign_in_page.find_sign_in_text().text)
    print("Passkey button text:", context.sign_in_page.find_passkey_button().text)


