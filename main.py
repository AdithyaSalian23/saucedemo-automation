from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
).click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
).click()

driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "finish"))
).click()

confirmation = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
)
message = confirmation.text
assert "Thank you for your order!" in message

print("✅ E2E Test Passed!")

driver.quit()
