from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def basket_should_change_after_adding_to_basket(self):
        self.should_be_product_gallery()
        self.add_product_to_basket()
        self.compare_prices()

    def should_be_product_gallery(self):
        assert self.is_element_present(*ProductPageLocators.MAIN_PRODUCT_GALLERY), 'No gallery on the product page'

    def add_product_to_basket(self):
        assert self.click(*ProductPageLocators.MAIN_PRODUCT_ADD_BASKET_BUTTON), "Can't add to basket, there's no button"

    def compare_prices(self):
        assert self.get_value(*ProductPageLocators.MAIN_PRODUCT_PRICE) in \
               self.get_value(*ProductPageLocators.BASKET_MINI), 'Total price in basket is not equal to product price'
