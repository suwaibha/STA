from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()

file_path = os.path.abspath("duplicate.html")
driver.get("file:///" + file_path.replace("\\","/"))

wait = WebDriverWait(driver,10)

# ---------- Add First Student ----------

usn = wait.until(
    EC.visibility_of_element_located((By.ID,"usn"))
)

name = driver.find_element(By.ID,"name")

usn.send_keys("1BM22CS101")
name.send_keys("Alice")

driver.find_element(By.ID,"addBtn").click()

time.sleep(2)

message = driver.find_element(By.ID,"message").text

print("First Attempt :", message)

assert message == "Student Added Successfully."

# ---------- Try Duplicate ----------

usn = driver.find_element(By.ID,"usn")
name = driver.find_element(By.ID,"name")

usn.send_keys("1BM22CS101")
name.send_keys("Bob")

driver.find_element(By.ID,"addBtn").click()

time.sleep(2)

message = driver.find_element(By.ID,"message").text

print("Second Attempt :", message)

assert message == "Duplicate USN not allowed."

print("\nPASS : Duplicate record rejected successfully.")

input("\nPress Enter to close browser...")

driver.quit()