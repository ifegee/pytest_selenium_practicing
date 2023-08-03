from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def have_message_with_continue_shopping_link(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_LINK_TO_SHOPPING), 'No link to continue shopping in basket'

    def should_not_have_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), 'Some products are in basket'
