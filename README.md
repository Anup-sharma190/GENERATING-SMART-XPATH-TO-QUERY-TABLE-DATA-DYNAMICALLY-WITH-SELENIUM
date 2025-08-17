# GENERATING-SMART-XPATH-TO-QUERY-TABLE-DATA-DYNAMICALLY-WITH-SELENIUM
# Selenium Project: Smart XPath Generation to Query Table Data

This project demonstrates how to dynamically generate smart XPath queries using **Selenium WebDriver** in Python.  
The script downloads an Excel file, uploads it back to the site, and queries table data dynamically by locating columns based on their header names (instead of hardcoding XPath).

## 🔹 Features
- Automates file **download** and **upload** using Selenium.
- Uses **dynamic XPath generation** to locate table cells.
- Implements **WebDriverWait** for stable execution.
- Prints confirmation messages and queried values.

## 🔹 Tech Stack
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- openpyxl (for Excel handling)

## 🔹 Setup & Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/selenium-smart-xpath-query.git
   cd selenium-smart-xpath-query
