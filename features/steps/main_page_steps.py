from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*='utilityNav']")
ABOUT_TARGET = (By.CSS_SELECTOR, 'a[href="https://corporate.target.com/about"]')
EXPLORE_AREAS = (By.XPATH, '//*[contains(text(), "Explore other areas of Target")]')
CIRCLE_ELEMENTS = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
#
# @given('Open target main page')
# def open_target_main(context):
#     context.driver.get('https://www.target.com/')
#     context.driver.wait.until(
#         EC.element_to_be_clickable(SEARCH_FIELD),
#         message='Search field not clickable'
#     )
#
# @when('Search for {search_word}')
# def search_product(context, search_word):
#     context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
#     context.driver.find_element(*SEARCH_BTN).click()
#     sleep(7)
#
#
# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(*CART_ICON).click()
#
#
# @then('Verify at least 1 link shown')
# def verify_1_header_link_shown(context):
#     link = context.driver.find_element(*HEADER_LINKS)
#     print(link)
#
#
# @then('Verify {link_amount} links shown')
# def verify_all_header_links_shown(context, link_amount):
#     link_amount = int(link_amount) # "6" => int 6
#     links = context.driver.find_elements(*HEADER_LINKS)
#     print(links)
#     assert len(links) == link_amount, f'Expected {link_amount} links, but got {len(links)}'
#
#
#
#     @given('Open target main page')
#     def open_main(context):
#         context.driver.get('https://www.target.com/')
#         sleep(10)
#
#     @when('Click on About Target')
#     def click_about(context):
#         context.wait.until(EC.element_to_be_clickable(ABOUT_TARGET)).click()
#         print(f'Clik {ABOUT_TARGET}')
#
#     @then('Verify Explore other areas of Target')
#     def verify_explore(context):
#         context.wait.until(EC.visibility_of_element_located(EXPLORE_AREAS))
#
#         expected_result = 'Explore other areas of Target'
#         actual_result = context.driver.find_element(*EXPLORE_AREAS).text
#         assert expected_result in actual_result, f'Expected {expected_result} did not match actual {actual_result}'


@given("I open the Target Circle page")
def open_main_circle(context):
    context.driver.get("https://www.target.com/l/target-circle/-/N-pzno9")

@when("I wait for the benefit cells to load")
def verify_elements(context):
    context.driver.wait.until(EC.visibility_of_element_located(CIRCLE_ELEMENTS))
    message = 'Benefit cells not visible'


@then("I should see at least 10 benefit cells on the page")
def benefit_cells(context):
    cells = context.driver.find_elements(*CIRCLE_ELEMENTS)
    assert len(cells) >= 10, f"Expected at least 10 benefit cells, but found {len(cells)}"
