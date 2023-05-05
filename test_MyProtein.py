from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time 

# def testSeleniumMyProtein():
    
try:
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome (service=service)
    driver.maximize_window()
    driver.get("https://www.myprotein.com.sg/sports-nutrition/clear-whey-isolate/12081395.html")

    try:
        cookiesAccept = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        cookiesAccept.click()
        bannerClose = driver.find_element(By.CLASS_NAME, 'close-button')
        bannerClose.click()

    finally:

        flavourChoices = driver.find_element(By.ID, 'athena-product-variation-dropdown-5')
        flavourChoices.click()
        # flavourChoices.send_keys("L")
        # flavourChoices.send_keys('Return')

        # promotionBanner = driver.find_element(By.class, "stripBanner")

        # driver.save_screenshot("testScreenshot.png")

except:
    print("Error! Page had issues loading...")

finally:
    time.sleep(3)
    driver.quit()
    print("Automation completed successfully!")
