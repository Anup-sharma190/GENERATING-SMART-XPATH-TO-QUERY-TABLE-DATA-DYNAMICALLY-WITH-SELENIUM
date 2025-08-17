"""
Project: Generating Smart XPath to Query Table Data Dynamically with Selenium
Author: Anup
Description:
    - This script demonstrates how to dynamically generate smart XPaths
      to locate table data (like Price of a given fruit) instead of hardcoding.
    - Covers file upload/download, dynamic locators, and toast validation.
"""

# ===================== Step 1: Import Required Libraries =====================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ===================== Step 2: Set File Path Variables =====================
file_path = r"C:\Users\Comp10\PycharmProjects\PythonProject\china.xlsx"
fruit_name = "Apple"   # Fruit to query dynamically

# ===================== Step 3: Launch Chrome Browser =====================
driver = webdriver.Chrome()
driver.implicitly_wait(20)

# ===================== Step 4: Open Target Website =====================
driver.get("https://rahulshettyacademy.com/upload-download-test/")

# ===================== Step 5: Download Excel File =====================
driver.find_element(By.ID, "downloadButton").click()

# ===================== Step 6: Upload Updated Excel File =====================
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

# ===================== Step 7: Wait for Toast Message =====================
wait = WebDriverWait(driver, 30)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(EC.visibility_of_element_located(toast_locator))

# ===================== Step 8: Capture and Print Toast Message =====================
toast_message = driver.find_element(*toast_locator).text
print("Upload Confirmation Message:", toast_message)

# ===================== Step 9: Generate Smart XPath for Price Column =====================
# Step 9.1 → Get column id of "Price" dynamically
price_column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")

# Step 9.2 → Build smart XPath for fruit price using fruit name + column id
price_xpath = f"//div[text()='{fruit_name}']/parent::div/parent::div/div[@id='cell-{price_column}-undefined']"

# Step 9.3 → Locate price element dynamically
actual_price = driver.find_element(By.XPATH, price_xpath).text

# ===================== Step 10: Print Result =====================
print(f"Price of {fruit_name}:", actual_price)

# ===================== Step 11: Close Browser =====================
driver.quit()
