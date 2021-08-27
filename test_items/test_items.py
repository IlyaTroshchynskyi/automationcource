import time
import pytest
from selenium.common.exceptions import NoSuchElementException



def test_button_add_bucket(browser, request):
    user_language = request.config.getoption('language')
    link = f'http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    try:
        element = browser.find_element_by_css_selector("#add_to_basket_form button").text
    except NoSuchElementException:
        element = ''
    assert len(element) > 1

