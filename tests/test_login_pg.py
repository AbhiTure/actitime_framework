from datetime import datetime
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.login_page import LogPage


data  = [("admin", "manage"), ("admin", "trainee"), ("trainee", "trainee")]
@pytest.mark.parametrize("username, password", data)
def test_login(initialize_driver,username, password):
    driver = initialize_driver
    try:
        lp = LogPage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_login_btn()

        wait_ = WebDriverWait(driver,  10)

        """validating login thourgh url"""
        # wait_.until((EC.url_to_be("https://demo.actitime.com/user/submit_tt.do")))

        """validate through title"""
        wait_.until(EC.title_is("actiTIME - Enter Time-Track"))

    except Exception as error_msg:
        td = datetime.now()
        screenshots_path = r"C:\Users\ASUS\PycharmProjects\framework_actitime\screenshots\\"
        name = f"screenshot-{td.day}-{td.month}-{td.year}-{td.hour}-{td.minute}-{td.second}.png"
        driver.save_screenshot(screenshots_path + name)
        raise error_msg
