from dotenv import load_dotenv

load_dotenv()
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

MY_EMAIL = "grossmaria38@gmail.com"
PASSWORD = os.environ["PASSWORD"]
JOBS_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2729074955&f_AL=true&geoId=102257491&keywords=sales" \
           "%20manager&location=London%2C%20England%2C%20United%20Kingdom "
phone = "542376985"

chrome_driver_path = "./chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(JOBS_URL)
time.sleep(3)
driver.find_element_by_class_name("nav__button-secondary").click()
username = driver.find_element_by_id("username")
username.send_keys(MY_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(3)
jobs_list = driver.find_elements_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li')
for job in jobs_list:
    try:
        job.click()
        time.sleep(2)
        driver.find_element_by_css_selector("div .jobs-apply-button--top-card button").click()
        time.sleep(1.5)
        driver.find_element_by_css_selector("button[aria-label='Submit application']").click()
    except (NoSuchElementException, ElementClickInterceptedException):
        print("The job is not relevant")
        driver.find_element_by_xpath('/html/body/div[3]/div/div/button').click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[3]/button[2]').click()

