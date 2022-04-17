 from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    x1=x.text
    x2=y.text
    z = int(x1) + int(x2)
    z1=str(z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z1)
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()