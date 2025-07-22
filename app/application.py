from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from pages.side_menu_page import SideMenu


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.cart_page = CartPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.side_menu_page = SideMenu(driver)
        self.product_page = ProductPage(driver)

