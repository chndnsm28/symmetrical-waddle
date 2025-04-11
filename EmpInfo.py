import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class EmpInfo:
    def __init__(self, driver):
        self.driver = driver
        self.movetoelement = (By.XPATH,
                                                   "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
        self.click_PIM = (By.CSS_SELECTOR,
                            "button[class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.firstname = (By.NAME, "firstName")

        self.middlename = (By.NAME, "middleName")
        self.lastname = (By.NAME, "lastName")
        self.addemp_button = (By.XPATH, "//button[@type = 'submit']")
        self.addempclick = (By.LINK_TEXT, "Add Employee")
        self.emplistclick = (By.LINK_TEXT, "Employee List")
        self.empDatas=  (By.XPATH, "//div/div[3][@class = 'oxd-table-cell oxd-padding-cell']/div")
        self.logoutoption = (By.CSS_SELECTOR, "p[class='oxd-userdropdown-name']")
        self.logoutclick = (By.LINK_TEXT, "Logout")





    def emp_operations(self, firstname, middlename, lastname):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*self.movetoelement)).click().perform()
        self.driver.find_element(*self.click_PIM ).click()
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.middlename).send_keys(middlename)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.addemp_button).click()
        self.driver.find_element(*self.addempclick).click()
        self.driver.find_element(*self.emplistclick).click()
        datas = self.driver.find_elements(*self.empDatas)
        time.sleep(2)
        #expected_names = ['Abhi Ram', 'Akruth Jain', 'AAnand Patil', 'Akhil D']
        expected_names = [firstname +' '+ middlename]
        print(expected_names)
        names = []

        for data in datas:
            names.append(data.text)
        for name in expected_names:
            if name in names:
                print("name verified")
            else:
                print("name not found")
        time.sleep(2)
        self.driver.find_element(*self.logoutoption).click()
        self.driver.find_element(*self.logoutclick).click()