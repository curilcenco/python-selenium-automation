from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class ProductPage:


    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    VIEW_CARD_CHECK_OUT_BTT = (By.CSS_SELECTOR, "[href='/cart']")
    PRODUCT_IN_CART_HEAD = (By.ID, 'cart-summary-heading')
    NAME_PRODUCT_IN_CART = (By. CSS_SELECTOR, "[data-test='cartItem-title']")
    ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    ADD = (By.ID, 'ad-link')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_add_to_cart(self):
        sleep(10)
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN))

    def click_add_to_cart(self, *ADD_TO_CART_BTN):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def click_add_to_cart_side(self):
        self.driver.find_element(*self.ADD_TO_CART_SIDE_NAV_BTN).click()

    def click_view_card(self):
        self.driver.find_element(*self.VIEW_CARD_CHECK_OUT_BTT).click()

    def get_product_name(self, *locator):
        return self.driver.find_element(*self.ADD_TO_CART_SIDE_NAV_BTN).text

    def open_product_page(self, *locator):
        self.driver.get(*locator).click()

    def click_product_link(self, *locator):
        self.driver.find_element( *locator).click()

    def get_product_name_click(self, locator):
        self.driver.find_element(*locator).click()

    def verify_product_name(self, expected_name, locator):
        actual_product_name = self.driver.find_element(*locator).text
        return expected_name == actual_product_name

    def product_exists_in_cart(self, *NAME_PRODUCT_IN_CART):
        element = self.driver.find_element(*self.NAME_PRODUCT_IN_CART)
        assert element, "No products found in cart"

    def verify_products_name_i(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        products = self.driver.find_elements(*self.LISTINGS)
        assert len(products) > 0, "No products found"

        for product in products:
            assert product.find_element(*self. PRODUCT_TITLE).text != "", "Missing product title"
            product.find_element(*self.PRODUCT_IMG)