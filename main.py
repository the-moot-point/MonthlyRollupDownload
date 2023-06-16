from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import calendar

def date_range():
    now = datetime.now()
    ranges = []
    for i in range(1, 9):
        first_day_prev_month = now.replace(day=1) - timedelta(days=i)
        _, last_day = calendar.monthrange(first_day_prev_month.year, first_day_prev_month.month)
        start_date = first_day_prev_month.strftime('%b %d, %Y 12:00 AM')
        end_date = first_day_prev_month.replace(day=last_day).strftime('%b %d, %Y 11:59 PM')
        ranges.append((start_date, end_date))
    return ranges

def download_month_data(driver, start_date, end_date):
    # Navigate to the URL
    driver.get(url)

    # Fill in login form (replace 'username' and 'password' with your actual login credentials)
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")

    username_field.send_keys("username")
    password_field.send_keys("password")

    # Submit login form
    password_field.send_keys(Keys.RETURN)

    # Wait until the page has loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "DateTimePicker-dateText")))

    # Change start and end date elements using JavaScript
    start_date_element = driver.find_element_by_css_selector("div[data-testid='ui-datetimepicker-start-text-value']")
    end_date_element = driver.find_element_by_css_selector("div[data-testid='ui-datetimepicker-end-text-value']")

    driver.execute_script("arguments[0].innerText = '{}';".format(start_date), start_date_element)
    driver.execute_script("arguments[0].innerText = '{}';".format(end_date), end_date_element)

    # Click on the "Download CSV" button
    download_button = driver.find_element_by_css_selector("div[data-testid='report-export-modal-download-csv-button']")
    download_button.click()

    # Click on the "Export" button to initiate the download
    export_button = driver.find_element_by_css_selector("button[data-testid='report-export-modal-export-button']")
    export_button.click()

url = "https://cloud.samsara.com/o/75184/fleet/reports/safety/dashboard/summary?duration=2627999.999&end_ms=1686927599999"

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\path\to\download\directory",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)

for start_date, end_date in date_range():
    download_month_data(driver, start_date, end_date)
