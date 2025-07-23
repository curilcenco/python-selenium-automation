from time import sleep

from behave import given, when, then


# @given('Open Help page for Returns')
# def click_cart(context):
#     context.app.help_page.open_help_returns()
#
#
# @when('Select Help topic {option_value}')
# def select_topic(context, option_value):
#     context.app.help_page.select_topic(option_value)
#
#
# # @then('Verify help Returns page opened')
# # def verify_returns_opened(context):
# #     context.app.help_page.verify_returns_opened()
# #
# #
# # @then('Verify help Current promotions page opened')
# # def verify_promotions_opened(context):
# #     context.app.help_page.verify_promotions_opened()
#
# @then('Verify help {header} page opened')
# def verify_correct_help_page_opened(context, header):
#     context.app.help_page.verify_correct_help_page_opened(header)
#
#
#
#
# @given('Open Help page Returns')
# def click_cart(context):
#     context.app.help_page.open_help_returns()
#
#
# @when('Select Help topic {option_value}')
# def select_topic(context, option_value):
#     context.app.help_page.select_topic(option_value)
#
#
# # @then('Verify help Returns page opened')
# # def verify_returns_opened(context):
# #     context.app.help_page.verify_returns_opened()
# #
# #
# # @then('Verify help Current promotions page opened')
# # def verify_promotions_opened(context):
# #     context.app.help_page.verify_promotions_opened()
#
# @then('Verify help {header} page opened')
# def verify_correct_help_page_opened(context, header):
#     context.app.help_page.verify_correct_help_page_opened(header)


@given('User is on the Target Help page')
def open_help(context):
    context.app.help_page.open_help_page()


@when('Verify input field')
def verify_input_field(context):
    context.app.help_page.verify_dropdown_help()


@when('User inputs "order" in search input field')
def input_order(context):
    context.app.help_page.send_text_dropdown('order')

    sleep(5)

@then('Verify dropdown help appear')
def verify_dropdown_help(context):
    context.app.help_page.verify_dropdown_help()

# @then('The "Track my order" help page should open')
# def verify_track_my_order(context):
#     context.app.help_page.verify_track_my_order()

@then('Dropdown selection click')
def verify_select_works(context):
    context.app.help_page.click_dropdown_help_element()

    sleep(5)

@then('Opens the correct url')
def open_correct_url(context):
    context.app.help_page.verify_partial_url_help('help/article')









