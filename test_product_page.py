import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('product', ['the-shellcoders-handbook_209/?promo=newYear',
                                     'coders-at-work_207/?promo=newYear2019'])
def test_guest_can_add_product_to_basket(browser, product):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/{product}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_gallery()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_prices()
