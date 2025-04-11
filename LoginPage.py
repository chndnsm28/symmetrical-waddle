from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.user_password = (By.NAME, "password")
        self.button_click = (By.CSS_SELECTOR, "button[type='submit']")



    def login(self):
        self.driver.find_element(*self.username_input).send_keys("Admin")
        self.driver.find_element(*self.user_password).send_keys("admin123")
        self.driver.find_element(*self.button_click).click()



