from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
COLOR_OPTION = (By.CSS_SELECTOR, "li[class^='styles_ndsCarouselItem'] a")
SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
SEARCH_BUTTON = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id^='addToCartButtonOrTextIdFor']")
ADD_TO_CART_SIDE_BUTTON = (By.CSS_SELECTOR,"[data-test='orderPickupButton']")
ADDED_IN_SIDE_CARD = (By.XPATH, "//*[@data-test='modal-drawer-heading' or contains(text(),'Added to cart')]")



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


@given ('I open the Target homepage')
def open_page(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when ('I search for a product "toothbrush"')
def search_product(context):
        search_box = context.driver.find_element(*SEARCH_FIELD)
        search_box.clear()
        search_box.send_keys("toothbrush" + Keys.ENTER)

@when ('Click search')
def click_search(context):
    context.driver.find_element(*SEARCH_BUTTON).click()

@when ('I add the first product to the cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON)
    sleep(1)

@when('Click Side Menu add')
def click_side_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON)
    sleep(8)

@when ('Added to the cart')
def check_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()

@when('Click Side Menu Btt')
def click_side_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_SIDE_BUTTON).click()
    sleep(2)


@then('Added in cart')
def added_in_cart(context):
    WebDriverWait(context.driver, 2).until(
        EC.visibility_of_element_located(ADDED_IN_SIDE_CARD)
    )
    # actual_result = context.driver.find_element(*ADDED_IN_SIDE_CARD).text.strip()
    # expected_result = ADDED_IN_SIDE_CARD
    #
    # assert expected_result in actual_result, f"Expected '{expected_result}' not found in actual '{actual_result}'"
    #
