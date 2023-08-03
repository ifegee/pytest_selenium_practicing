from .base_page import BasePage
from .locators import BasePageLocators, ProductPageLocators


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
               self.get_value(*BasePageLocators.BASKET), 'Total price in basket is not equal to product price'

    def compare_product_names_main_breadcrumbs(self):
        product_name = self.get_value(*ProductPageLocators.PRODUCT_NAME)
        breadcrumbs_name = self.get_value(*BasePageLocators.BREADCRUMBS_PRODUCT_NAME)
        assert product_name == breadcrumbs_name, f'Product name in breadcrumbs {breadcrumbs_name!r} not equal ' \
                                                 f'{product_name!r} in the main product name'

    def compare_product_names_main_alert(self):
        product_name = self.get_value(*ProductPageLocators.PRODUCT_NAME)
        product_name_alert = self.get_value(*ProductPageLocators.PRODUCT_NAME_ALERT)
        assert product_name == product_name_alert, \
            f'Product name in alert {product_name_alert!r} not equal {product_name!r} in the main product name'

    def success_message_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
