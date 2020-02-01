from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')

    for n, element in enumerate(elements):
        element.send_keys('test ' + str(n))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
