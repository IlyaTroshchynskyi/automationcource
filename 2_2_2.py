import time
import math
from selenium import webdriver


# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и
# огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
#     Открыть страницу http://SunInJuly.github.io/execute_script.html.
#     Считать значение для переменной x.
#     Посчитать математическую функцию от x.
#     Проскроллить страницу вниз.
#     Ввести ответ в текстовое поле.
#     Выбрать checkbox "I'm the robot".
#     Переключить radiobutton "Robots rule!".
#     Нажать на кнопку "Submit".


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)
    num1 = browser.find_element_by_id("input_value").text

    res = math.log(abs(12*math.sin(int(num1))))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(res))
    input2 = browser.find_element_by_id('robotCheckbox')
    input2.click()
    input3 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", input3)
    input3.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()