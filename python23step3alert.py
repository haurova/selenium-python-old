from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os 
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(int(x)))))

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

link = "http://suninjuly.github.io/alert_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()

 # не забываем оставить пустую строку в конце файла
