from selenium import webdriver
import time

# Ваши шаги:
#
#   В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
#   Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit.
#   XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы
#   он работал.
#   Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
#   Запустите ваш код.



link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Firefox(executable_path
                                ='/home/myadmin/PycharmProjects/geckodriver')
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
