from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
from math import log, sin
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

def calc(x):
  return str(log(abs(12*sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
   # x = browser.find_element_by_id('input_value').text
   # y = calc(x)

    textfield = browser.find_element_by_id('answer').send_keys(file_path)

    print(os.path.abspath(os.path.dirname(__file__)))
   # checkbox = browser.find_element_by_id('robotCheckbox')
    #checkbox.click()
    #radio = browser.find_element_by_id('robotsRule')
   # browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
   # radio.click()

   # button = browser.find_element_by_css_selector("button.btn")
    
    #button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()

 # не забываем оставить пустую строку в конце файла
