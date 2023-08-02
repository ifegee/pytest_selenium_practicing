from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
