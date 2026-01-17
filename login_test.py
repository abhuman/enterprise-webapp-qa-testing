from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

driver.find_element(By.ID, "username").send_keys("test_user")
driver.find_element(By.ID, "password").send_keys("Test@123")
driver.find_element(By.ID, "loginBtn").click()

time.sleep(3)
assert "Dashboard" in driver.title

driver.quit()
