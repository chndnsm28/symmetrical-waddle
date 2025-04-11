import json
import os
import sys
import pytest
sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) ) )
from PageObjects.EmpInfo import EmpInfo
from PageObjects.LoginPage import LoginPage

testdata_path = '../Data/test_e2eEmpData.json'
with open(testdata_path, 'r') as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_code,test_list_item):
    driver = browser_code
    driver.implicitly_wait(5)
    loginpage= LoginPage(driver)
    loginpage.login()
    empinfo = EmpInfo(driver)
    empinfo.emp_operations(test_list_item["first_name"],test_list_item["middle_name"],test_list_item["last_name"])











