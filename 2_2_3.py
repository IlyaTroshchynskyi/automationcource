import time
import os
from selenium import webdriver


# Задание: загрузка файла
#
# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
#     Открыть страницу http://suninjuly.github.io/file_input.html
#     Заполнить текстовые поля: имя, фамилия, email
#     Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#     Нажать кнопку "Submit"


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('TTT')
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys('fdfdf')
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(cur_dir, "../theory.txt")
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()