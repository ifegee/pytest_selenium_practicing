from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-default:nth-child(1)')
    BASKET = (By.CSS_SELECTOR, '.basket-mini')
    BREADCRUMBS_PRODUCT_NAME = (By.CSS_SELECTOR, '.breadcrumb .active')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK_TO_SHOPPING = (By.CSS_SELECTOR, '#content_inner > p > a')
    BASKET_TITLE = (By.CSS_SELECTOR, '.basket-title')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    MAIN_PRODUCT_ADD_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MAIN_PRODUCT_GALLERY = (By.CSS_SELECTOR, '#product_gallery')
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
