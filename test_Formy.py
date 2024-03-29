from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


def testSeleniumFormy():
    try:
        service = ChromeService(
            executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://formy-project.herokuapp.com/form")

        firstName = driver.find_element(By.ID, "first-name")
        firstName.clear()
        firstName.send_keys("Insert Random First Name ABC...")

        lastName = driver.find_element(By.ID, "last-name")
        lastName.clear()
        lastName.send_keys("Insert Random  Last Name XYZ...")

        jobTitle = driver.find_element(By.ID, "job-title")
        jobTitle.clear()
        jobTitle.send_keys("Testing Random Job...")

        educationFirst = driver.find_element(By.ID, 'radio-button-1')
        educationFirst.click()

        educationSecond = driver.find_element(By.ID, 'radio-button-2')
        educationSecond.click()

        educationThird = driver.find_element(By.ID, 'radio-button-3')
        educationThird.click()

        sexMale = driver.find_element(By.ID, 'checkbox-1')
        sexMale.click()

        sexFemale = driver.find_element(By.ID, 'checkbox-2')
        sexFemale.click()

        sexPreferNotToSay = driver.find_element(By.ID, 'checkbox-3')
        sexPreferNotToSay.click()

        yearsOfExperience = driver.find_element(By.ID, 'select-menu')
        yearsOfExperience.click()
        yearsOfExperience.send_keys("2")
        yearsOfExperience.send_keys('Return')

        dateOfSubmission = driver.find_element(By.ID, 'datepicker')
        dateOfSubmission.click()
        dateOfSubmission.send_keys('Return')
        time.sleep(3)

        submitForm = driver.find_element(By.LINK_TEXT, 'Submit')
        submitForm.click()

        driver.save_screenshot("testFormyScreenshot.png")

    except:
        print("Error! Page had issues loading...")

    finally:
        time.sleep(3)
        driver.quit()
