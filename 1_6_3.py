from selenium import webdriver
import time

# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего
# продукта. В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно
# переусердствовали, добавив в форму 100 обязательных полей и ограничив время на ее заполнение

try:
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла