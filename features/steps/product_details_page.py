from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'





from behave import given, when, then
from time import sleep


# @then('Verify search results shown for {product}')
# def verify_search_results(context, product):
#     context.app.search_results_page.verify_search_results(product)
#
#
# @then('Verify search term {product} in URL')
# def verify_search_url(context, product):
#     context.app.search_results_page.verify_search_url(product)
@given('Open target main')
def open_cart(context):
    context.driver.get('https://www.target.com/')

@when('Add product to cart from search results')
def click_add_to_c(context):
    context.app.product_page.click_add_to_cart()


@when('Store product info')
def store_product_name(context):
    locator = context.app.search_results_page.PRODUCT_NAME
    context.product_name = context.app.search_results_page.get_product_name_click(locator)
    print(f'Product stored: {context.product_name}')


@when('Confirm Add Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.search_results_page.get_product_name_click()
    # context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN)
    sleep(4)


@then('Verify that every product has name and image')
def verify_products_name_img(context):
    context.app.product_page.verify_products_name_i()
