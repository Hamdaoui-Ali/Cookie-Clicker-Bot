from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import os

#number of clicks deserved
numClicks = int(input("Enter the number of clicks deserved : "))

#installing the webdriver for chrome browser
service = ChromeService(ChromeDriverManager().install())

#initializing the chrome webdriver
driver = webdriver.Chrome(service=service)

def Cookie_Clicker_Bot(numClicks):
    try:
    #pointing on the website
        driver.get("https://orteil.dashnet.org/")
        time.sleep(4)


        cookieClicker = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Cookie Clicker')]"))
        )
        cookieClicker.click()
        time.sleep(2)

        languageChoice = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
        )
        languageChoice.click()
        time.sleep(2)

        cookies = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.ID, 'bigCookie'))
        )

        for i in range(numClicks):
            cookies.click()
            time.sleep(0.1)

            numCookies = driver.find_element(By.ID, 'cookies').text
            numGrandma = driver.find_element(By.ID, 'productPrice1').text
            numCursor = driver.find_element(By.ID, 'productPrice0').text
            cursor = driver.find_element(By.ID, 'product0')
            grandma = driver.find_element(By.ID, 'product1')

            numCookies = re.findall(r'\d+', numCookies)
            numCookies = int(numCookies[0])

            numGrandma = re.findall(r'\d+', numGrandma)
            numGrandma = int(numGrandma[0])

            numCursor = re.findall(r'\d+', numCursor)
            numCursor = int(numCursor[0])
            
            if numCookies >= numCursor:
                if numCursor < numGrandma:
                    cursor.click()
                else:
                    grandma.click()

        time.sleep(2)
        driver.quit()

    except Exception as e:
        print(f"There is a problem with the website, error type : {e}")


Cookie_Clicker_Bot(numClicks)

