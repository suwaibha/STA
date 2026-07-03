from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Launch Chrome
driver = webdriver.Chrome()

driver.maximize_window()

# Open HTML File
file_path = os.path.abspath("sorting.html")
driver.get("file:///" + file_path.replace("\\", "/"))

# Explicit Wait
wait = WebDriverWait(driver,10)

wait.until(
    EC.visibility_of_element_located((By.ID,"studentTable"))
)

# ---------------- ASCENDING SORT ----------------

print("Checking Ascending Order...\n")

driver.find_element(By.ID,"nameHeader").click()

time.sleep(2)

rows = driver.find_elements(By.XPATH,"//*[@id='studentTable']/tbody/tr/td[2]")

ascending=[]

for row in rows:
    ascending.append(row.text)

print("Ascending Order:")
print(ascending)

expected = sorted(ascending)

assert ascending == expected

print("\nPASS : Ascending Sorting Correct")

# ---------------- DESCENDING SORT ----------------

driver.find_element(By.ID,"nameHeader").click()

time.sleep(2)

rows = driver.find_elements(By.XPATH,"//*[@id='studentTable']/tbody/tr/td[2]")

descending=[]

for row in rows:
    descending.append(row.text)

print("\nDescending Order:")
print(descending)

expected = sorted(descending, reverse=True)

assert descending == expected

print("\nPASS : Descending Sorting Correct")

print("\nAutomation Completed Successfully!")

input("\nPress Enter to Close Browser...")

driver.quit()