import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_gallery()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_prices()
    page.compare_product_names_main_breadcrumbs()
    page.compare_product_names_main_alert()
