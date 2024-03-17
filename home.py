import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.automationtesting.in/")

#Задание 1 слайд 94
driver.execute_script("window.scrollBy(0, 600);")
btn_Selenium_Ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 h3")
btn_Selenium_Ruby.click()
btn_reviews = driver.find_element_by_css_selector(".reviews_tab > a")
btn_reviews.click()
btn_5stars = driver.find_element_by_class_name("star-5")
btn_5stars.click()
add_coment = driver.find_element_by_id("comment")
add_coment.send_keys("Nice book!")
add_name = driver.find_element_by_id("author")
add_name.send_keys("Tester")
add_email = driver.find_element_by_id("email")
add_email.send_keys("tester@contoso.com")
btn_submit = driver.find_element_by_id("submit")
btn_submit.click()


driver.quit()

