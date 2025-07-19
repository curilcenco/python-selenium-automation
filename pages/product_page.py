from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    CART_EMPTY = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def get_product_name(self, *locator):
        return self.driver.find_element(*self.ADD_TO_CART_SIDE_NAV_BTN).text

    def open_product_page(self, *locator):
        self.driver.get(*locator).click()

    def click_product_link(self, *locator):
        self.driver.find_element(*locator).click()

    def click_cart_logo(self, *locator):
        self.driver.find_element(*self.CART_ICON).click()

    # def get_product_name_click(self, *locator):
    #     self.driver.find_element(*self.ADD_TO_CART_SIDE_NAV_BTN).click

    def verify_product_name(self, expected_name, locator):
        actual_product_name = self.driver.find_element(*locator).text
        return expected_name == actual_product_name

    def verify_products_name_i(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        products = self.driver.find_elements(*self.LISTINGS)
        assert len(products) > 0, "No products found"

        for product in products:
            assert product.find_element(*self.PRODUCT_TITLE).text != "", "Missing product title"
            product.find_element(*self.PRODUCT_IMG)

    def verify_empty_cart(self):
        el = self.wait.until(EC.visibility_of_element_located(self.CART_EMPTY))
        print('\nCart empty element found:')
        print(el)
        assert el.is_displayed(), "Empty cart message is not visible"
