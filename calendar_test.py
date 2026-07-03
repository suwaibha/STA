from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import os
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open HTML file
file_path = os.path.abspath("calendar.html")
driver.get("file:///" + file_path.replace("\\","/"))

wait = WebDriverWait(driver,10)

dateBox = wait.until(
    EC.visibility_of_element_located((By.ID,"interviewDate"))
)

# Yesterday
yesterday = (datetime.today()-timedelta(days=1)).strftime("%Y-%m-%d")

# Tomorrow
tomorrow = (datetime.today()+timedelta(days=1)).strftime("%Y-%m-%d")

print("Yesterday :", yesterday)
print("Tomorrow  :", tomorrow)

# ---------- Try Yesterday ----------

driver.execute_script(
    "arguments[0].value = arguments[1];",
    dateBox,
    yesterday
)

time.sleep(2)

value = dateBox.get_attribute("value")

minDate = dateBox.get_attribute("min")

print("\nMinimum Allowed Date :", minDate)
print("Selected Date :", value)

if value < minDate:
    print("PASS : Past date is not allowed.")
else:
    print("FAIL : Past date accepted.")

# ---------- Select Tomorrow ----------

driver.execute_script(
    "arguments[0].value = arguments[1];",
    dateBox,
    tomorrow
)

time.sleep(2)

value = dateBox.get_attribute("value")

print("\nSelected Future Date :", value)

if value == tomorrow:
    print("PASS : Future date accepted.")
else:
    print("FAIL : Future date not accepted.")

input("\nPress Enter to close browser...")

driver.quit()