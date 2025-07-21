import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
import os

# Configure logging
logging.basicConfig(filename='submission_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSV data
df = pd.read_csv("form_data.csv")

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH

# Path to the local HTML form
form_path = 'file:///' + os.path.abspath('test_form.html').replace("\\", "/")

# Iterate through each row of CSV
for index, row in df.iterrows():
    try:
        driver.get(form_path)
        time.sleep(1)

        driver.find_element(By.NAME, 'name').send_keys(row['name'])
        driver.find_element(By.NAME, 'email').send_keys(row['email'])
        driver.find_element(By.NAME, 'address').send_keys(row['address'])

        gender_xpath = f"//input[@name='gender'][@value='{row['gender'].strip().capitalize()}']"
        driver.find_element(By.XPATH, gender_xpath).click()
        
        if 'subscribe' in row and str(row['subscribe']).strip().lower() == 'yes':
            driver.find_element(By.NAME, 'subscribe').click()

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        logging.info(f"Row {index + 1}: Submitted successfully for {row['email']}")
        time.sleep(1)  

    except Exception as e:
        logging.error(f"Row {index + 1}: Failed for {row['email']}. Error: {str(e)}")
driver.quit()