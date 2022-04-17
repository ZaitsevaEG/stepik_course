def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time
import math
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector(".form-group .nowrap:nth-child(2)")
    x = x_element.text
    y = calc(x)
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()