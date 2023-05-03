from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

# def testSeleniumGoogle():

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome (service=service)
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
# elem = driver.find_element(By.NAME, 'q')
# elem.clear()
# elem.send_keys("Python")
# elemLucky = driver.find_element(By.NAME, 'btnI')
# elemLucky.click()
# driver.save_screenshot("tst.png")
time.sleep(3)
driver.quit()
