from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = MY_CHROME_DRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=100737633&keywords=qa%20engineer&location=San%20Diego%20County%2C%20California%2C%20United%20States")

wait = WebDriverWait(driver, 10)

# Perform Login
try:
    sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    sign_in_button.click()

    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.clear()
    username_input.send_keys(MY_EMAIL)
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(MY_PASSWORD)
    driver.find_element_by_css_selector("form button").click()

except TimeoutException:
    print("The page took so long to load")


# Get the job items
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.jobs-apply-button")))
jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# Save the first 3 jobs
for job in jobs[:3:]:
    job.click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.jobs-apply-button")))
    save_job_button = driver.find_element_by_css_selector("button.jobs-save-button span")
    if save_job_button.text == "Save":
        save_job_button.click()

driver.quit()
