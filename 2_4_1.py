import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
#     Открыть страницу http://suninjuly.github.io/explicit_wait2.html
#     Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
#     Нажать на кнопку "Book"
#     Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    if button:
        browser.find_element_by_id("book").click()

    num1 = browser.find_element_by_id("input_value").text

    res = math.log(abs(12 * math.sin(int(num1))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(res))

    button = browser.find_element_by_id("solve")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()