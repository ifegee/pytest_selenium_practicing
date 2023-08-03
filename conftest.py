import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsCH
from selenium.webdriver.firefox.options import Options as OptionsFF


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Choose language code, e.g. "es", "ru", "fr", etc.')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        options_ch = OptionsCH()
        # options_ch.add_argument('--headless')
        options_ch.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_ch)
    elif browser_name == 'firefox':
        options_ff = OptionsFF()
        options_ff.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_ff)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    browser.quit()
