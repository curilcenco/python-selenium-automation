from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep



COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
COLOR_OPTION = (By.CSS_SELECTOR, "li[class^='styles_ndsCarouselItem'] a")


# @given('Open target product {product_id} page')
# def open_target(context, product_id):
#     context.driver.get(f'https://www.target.com/p/{product_id}')
#     sleep(8)
#
#
# @then('Verify user can click through colors')
# def click_and_verify_colors(context):
#     expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
#     actual_colors = []
#
#     colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
#
#     for color in colors:
#         color.click()
#
#         selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
#         print('Current color', selected_color)
#
#         selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
#         actual_colors.append(selected_color)
#         print(actual_colors)
#
#     assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'



@given('Open target product page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/15oz-stoneware-westfield-mugs-threshold/-/A-82614298?preselect=82326611#lnk=sametab')
    sleep(2)


@then('Verify user can click through c')
def click_and_verify_colors(context):
    expected_colors = ['Blue', 'Gray', 'White', 'Navy  - Out of Stock']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTION)
    for color in colors:
        color.click()
        sleep(1)

    selected_color = context.driver.find_element(*SELECTED_COLOR).text
    print('Current color', selected_color)

    selected_color = selected_color.split('\n')[1]
    actual_colors.append(selected_color)
    print(actual_colors)

    assert expected_colors in actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'