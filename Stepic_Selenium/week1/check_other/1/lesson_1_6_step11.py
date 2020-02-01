from selenium import webdriver
import time

try:
    link_succ = "http://suninjuly.github.io/registration1.html"
    link_fail = 'http://suninjuly.github.io/registration2.html'

    browser = webdriver.Chrome()

    # browser.get(link_succ)
    browser.get(link_fail)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block input.first')
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_css_selector('.first_block input.second')
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_css_selector('.first_block input.third')
    input3.send_keys("Petrov@qwert.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
