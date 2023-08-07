import time
from generic.excel_libra import read_locators


file_path = r"C:\Users\ASUS\PycharmProjects\framework_actitime\project_file\actitime_locators.xlsx"
sheet_name = "login_objects"

class LogPage:
    """ Thisclasshold allthe functiion of  login page """
    locators = read_locators(file_path, sheet_name)

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,username):
        """entering username in username textfield"""
        self.driver.find_element(*self.locators["username_txt"]).send_keys(username)
        time.sleep(2)

    def enter_password(self,password):
        """entering username in password textfield"""
        self.driver.find_element(*self.locators["password_txt"]).send_keys(password)
        time.sleep(2)

    def click_login_btn(self):
        """ cleck  on  the  login btn """
        self.driver.find_element(*self.locators["login_btn"]).click()
        time.sleep(2)