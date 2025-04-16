from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https//websitename.com")
driver.find_element(By.ID, "Username").send_keys("xyz")
driver.find_element(By.XPATH, "//div[@class = 'password']").send_keys("password123")
driver.find_element(By.CLASS_NAME, "Button").click()
driver.find_element(By.CLASS_NAME, "hotels").click()
driver.find_element(By.LINK_TEXT, "Where do you want to stay?").send_keys("new york")
driver.find_element(By.CLASS_NAME, "checkInDate").send_keys("10/04/2025")
driver.find_element(By.CLASS_NAME, "checkOutDate").send_keys("15/04/2025")
driver.find_element(By.NAME, "gstSlct").click()
driver.find_element(By.NAME, "Submit").click()
driver.find_element(By.ID, "htl_id_seo_20080802125928557").click()
driver.find_element(By.ID, "Apply_coupon").send_keys("Summer25")
msg = driver.find_element(By.XPATH, "//div[@class ='cpnInput__success font11 redText appendTop5']").text
assert "success" in msg

