from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin


def calc(x):
  return str(log(abs(12*sin(int(x)))))

try: 
	browser = webdriver.Chrome()
	# говорим WebDriver ждать все элементы в течение 5 секунд

	browser.get("http://suninjuly.github.io/explicit_wait2.html")



	price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    	)
	button = browser.find_element_by_id('book')
	button.click()

	x = browser.find_element_by_id('input_value').text
	y = calc(x)


	textfield = browser.find_element_by_id('answer').send_keys(y)

	button = browser.find_element_by_id("solve")
	button.click()


finally:
	time.sleep(15)
	browser.quit()