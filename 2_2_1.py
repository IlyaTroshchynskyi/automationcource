import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# Напишите код, который реализует следующий сценарий:
#
#     Открыть страницу http://suninjuly.github.io/selects1.html
#     Посчитать сумму заданных чисел
#     Выбрать в выпадающем списке значение равное расчитанной сумме
#     Нажать кнопку "Submit"

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text

    num2 = browser.find_element_by_id('num2').text
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(int(num1)+int(num2)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()