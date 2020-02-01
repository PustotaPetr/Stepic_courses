from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def test(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first = browser.find_element_by_css_selector('input.form-control.first[required=""]')
        input_first.send_keys('Ivan')
        input_second = browser.find_element_by_css_selector('input.form-control.second[required=""]')
        input_second.send_keys('Ivanov')
        input_third = browser.find_element_by_css_selector('input.form-control.third[required=""]')
        input_third.send_keys('Ivanov@mail.ru')
        # Отправляем заполненную форму
        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if  __name__ == "__main__":
    test(link1)

    test(link2)
