# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# class TargetCircle:
#     CIRCLE_ELEMENTS = (By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 4)
#
#     def open_target_circle(self):
#         self.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
#
#     def find_elements_by(self, *CIRCLE_ELEMENTS):
#         elements = self.driver.find_elements(*CIRCLE_ELEMENTS)
#         return elements
#
#     def verify_circle_elements(self, CIRCLE_ELEMENTS):
#         self.wait.until(EC.visibility_of_element_located(CIRCLE_ELEMENTS))
#
#         expected_result = 'Explore other areas of Target'
#         actual_result = self.driver.find_element(*CIRCLE_ELEMENTS).text
#         assert expected_result in actual_result, f'Expected {expected_result} did not match actual {actual_result}'
