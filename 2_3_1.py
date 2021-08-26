import math
import time
from selenium import webdriver


# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#     Открыть страницу http://suninjuly.github.io/alert_accept.html
#     Нажать на кнопку
#     Принять confirm
#     На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
# вы увидите окно с
# числом. Отправьте полученное число в качестве ответа на это задание.


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    num1 = browser.find_element_by_id("input_value").text

    res = math.log(abs(12 * math.sin(int(num1))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(res))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()