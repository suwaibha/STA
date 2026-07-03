from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()

file_path = os.path.abspath("session.html")
driver.get("file:///" + file_path.replace("\\","/"))

wait = WebDriverWait(driver,10)

# Login
login_btn = wait.until(
    EC.element_to_be_clickable((By.TAG_NAME,"button"))
)

login_btn.click()

print("Login Successful")

print("Waiting for session timeout...")

time.sleep(11)        # Wait longer than 10-second timeout

# Perform Action
driver.find_element(By.ID,"actionBtn").click()

# Read alert
alert = wait.until(EC.alert_is_present())

print("Alert:", alert.text)

if alert.text == "Session Expired":
    print("PASS : Session Expired")

alert.accept()

time.sleep(1)

# Verify Login page displayed
login_page = driver.find_element(By.ID,"loginPage")

if login_page.is_displayed():
    print("PASS : Redirected to Login Page")
else:
    print("FAIL")

input("Press Enter to close...")

driver.quit()