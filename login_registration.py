import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Задание 2 слайд 95
btn_my_account = driver.find_element_by_id("menu-item-50")
btn_my_account.click()
reg_email = driver.find_element_by_id("reg_email")
reg_email.send_keys("tester3@contoso.com")
reg_password = driver.find_element_by_id("reg_password")
reg_password.send_keys("P@ssw0rd-tro-lo-lo")
btn_reg = driver.find_element_by_css_selector(".woocomerce-FormRow input:nth-child(3)")
btn_reg.click()

#Задание 3 слайд 96
btn_my_account = driver.find_element_by_id("menu-item-50")
btn_my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("tester@contoso.com")
passwd = driver.find_element_by_id("password")
passwd.send_keys("P@ssw0rd-tro-lo-lo")
btn_login = driver.find_element_by_name("login")
btn_login.click()

time.sleep(10)
driver.quit()