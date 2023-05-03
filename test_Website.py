from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time 

def testSeleniumFormy():
    try:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome (service=service)
        driver.maximize_window()
        driver.get("https://formy-project.herokuapp.com/form")

        firstName = driver.find_element(By.ID, "first-name")
        firstName.clear()
        firstName.send_keys("Insert Random First Name ABC...")

        # driver.save_screenshot("testScreenshot.png")

    except:
        print("Error! Page had issues loading...")

    finally:
        time.sleep(3)
        driver.quit()
