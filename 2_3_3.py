import math
import time
from selenium import webdriver



# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить
# WebDriver на новую вкладку и решить в ней задачу.
#
# Сценарий для реализации выглядит так:
#
#     Открыть страницу http://suninjuly.github.io/redirect_accept.html
#     Нажать на кнопку
#     Переключиться на новую вкладку
#     Пройти капчу для робота и получить число-ответ


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    browser.switch_to.window(browser.window_handles[1])

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