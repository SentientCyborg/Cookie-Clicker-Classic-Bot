import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


timer = time.time() + 5
five_mins = time.time() + 60 * 5

URL = "https://orteil.dashnet.org/experiments/cookie/"

# Add the path to your Chromedriver install
chrome_driver_path = Service("YOUR PATH HERE\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get(URL)
wait = WebDriverWait(driver, 1)
cookie = wait.until(EC.presence_of_element_located((By.ID, "cookie")))

while True:
    cookie.click()
    if time.time() > timer:
        timer = time.time() + 5

        store = driver.find_elements(By.CSS_SELECTOR, '#store div')
        available = [item.get_attribute('id') for item in store if item.get_attribute('class') == ""]
        if len(available) > 0:
            wait.until(EC.presence_of_element_located((By.ID, available[-1]))).click()

    if time.time() > five_mins:
        cookies_per_sec = driver.find_element(By.ID, 'cps').text
        print(cookies_per_sec)
        break
