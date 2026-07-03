from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open the local HTML file
file_path = os.path.abspath("students.html")
driver.get("file:///" + file_path.replace("\\", "/"))

# Explicit Wait
wait = WebDriverWait(driver, 10)

# Wait until the table is visible
wait.until(
    EC.visibility_of_element_located((By.ID, "studentTable"))
)

# -------------------- PAGE 1 --------------------

time.sleep(2)   # So you can see Page 1

rows = driver.find_elements(By.XPATH, "//*[@id='studentTable']/tbody/tr")

page1 = []

print("========== PAGE 1 ==========")

for row in rows:
    print(row.text)
    page1.append(row.text)

print("\nTotal Records on Page 1 :", len(page1))

page_no = driver.find_element(By.ID, "pageNo").text
print("Current Page :", page_no)

# -------------------- PAGE 2 --------------------

driver.find_element(By.ID, "next").click()

wait.until(
    EC.text_to_be_present_in_element((By.ID, "pageNo"), "2")
)

time.sleep(2)   # So you can see Page 2

rows = driver.find_elements(By.XPATH, "//*[@id='studentTable']/tbody/tr")

page2 = []

print("\n========== PAGE 2 ==========")

for row in rows:
    print(row.text)
    page2.append(row.text)

print("\nTotal Records on Page 2 :", len(page2))

page_no = driver.find_element(By.ID, "pageNo").text
print("Current Page :", page_no)

# -------------------- VALIDATION --------------------

print("\n========== VALIDATION ==========")

if len(page1) == 10:
    print("✔ PASS : Page 1 contains 10 records")
else:
    print("✘ FAIL : Page 1 does not contain 10 records")

if len(page2) == 10:
    print("✔ PASS : Page 2 contains 10 records")
else:
    print("✘ FAIL : Page 2 does not contain 10 records")

if page1 != page2:
    print("✔ PASS : Page 2 records are different from Page 1")
else:
    print("✘ FAIL : Same records are displayed")

if page_no == "2":
    print("✔ PASS : Page number updated successfully")
else:
    print("✘ FAIL : Page number did not update")

total_records = len(page1) + len(page2)

print("Total Student Records :", total_records)

print("\nAutomation Completed Successfully!")

# Keep browser open
input("\nPress Enter to close the browser...")

driver.quit()