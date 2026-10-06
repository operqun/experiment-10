import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 1. Launch Chrome (Selenium Manager finds the matching ChromeDriver automatically)
driver = webdriver.Chrome()
driver.set_window_size(1280, 1050)

# 2. Open the event registration form (page under test)
page = "file://" + os.path.abspath("event-registration/index.html")
driver.get(page)
print("Page title :", driver.title)
print("Current URL:", driver.current_url)

# 3. Locating elements using different locator strategies
heading  = driver.find_element(By.TAG_NAME, "h1")
subtitle = driver.find_element(By.CLASS_NAME, "sub")
name_box = driver.find_element(By.ID, "name")
gender   = driver.find_elements(By.NAME, "gender")
email    = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
register = driver.find_element(By.XPATH, "//button[text()='Register']")
print("By.TAG_NAME     h1           ->", heading.text)
print("By.CLASS_NAME   sub          ->", subtitle.text)
print("By.ID           name         -> placeholder:", name_box.get_attribute("placeholder"))
print("By.NAME         gender       ->", len(gender), "radio buttons")
print("By.CSS_SELECTOR email input  -> placeholder:", email.get_attribute("placeholder"))
print("By.XPATH        Register btn ->", register.text)

# 4. Interacting with elements
name_box.send_keys("Ravi Kumar")
email.send_keys("ravi@gmail.com")
driver.find_element(By.ID, "phone").send_keys("9876543210")
driver.find_element(By.ID, "college").send_keys("ABC Engineering College")
Select(driver.find_element(By.ID, "event")).select_by_visible_text("Hackathon")
driver.find_element(By.ID, "m").click()
driver.find_element(By.ID, "password").send_keys("ravi@123")
driver.find_element(By.ID, "terms").click()
print("Male selected  :", driver.find_element(By.ID, "m").is_selected())
print("Terms accepted :", driver.find_element(By.ID, "terms").is_selected())
register.click()

# 5. Reading the result and taking a screenshot
message = driver.find_element(By.ID, "success").text
print("Result message :", message)
driver.save_screenshot("registration_result.png")
print("Screenshot saved: registration_result.png")

# 6. Browser navigation commands
driver.refresh()
print("After refresh, Name field empty:", driver.find_element(By.ID, "name").get_attribute("value") == "")
time.sleep(1)
driver.quit()
print("Browser closed.")