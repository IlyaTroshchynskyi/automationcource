import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# нужно выполнить установку webdriver_manager пакета чтоб автоматически установился Firefox


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    browser.get(link)

    input1 = browser.find_element_by_tag_name('.first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys("Smolensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()