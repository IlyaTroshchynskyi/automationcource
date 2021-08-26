import math
import time
from selenium import webdriver


# Ваша программа должна:
#
#     Открыть страницу http://suninjuly.github.io/get_attribute.html.
#     Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
#     Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
#     Посчитать математическую функцию от x (сама функция остаётся неизменной).
#     Ввести ответ в текстовое поле.
#     Отметить checkbox "I'm the robot".
#     Выбрать radiobutton "Robots rule!".
#     Нажать на кнопку "Submit".

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)
    element = browser.find_element_by_id("treasure")
    x = element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()
    input3 = browser.find_element_by_id('robotsRule')
    input3.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()