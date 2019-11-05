from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    fname = browser.find_element_by_css_selector("input[name='firstname']").send_keys('hi')
    lname = browser.find_element_by_css_selector("input[name='lastname']").send_keys('ho')
    email = browser.find_element_by_css_selector("input[name='email']").send_keys('hi@hi.hi')
    file = browser.find_element_by_css_selector("input[name='file']").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()

 # не забываем оставить пустую строку в конце файла
