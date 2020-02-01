from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    span = browser.find_element_by_id("input_value")
    x = span.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check1 = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    check1.click()
    radio1 = browser.find_element_by_css_selector("[for='robotsRule']")
    radio1.click()
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    time.sleep(15)
    browser.quit()
