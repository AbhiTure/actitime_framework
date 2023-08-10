from datetime import datetime
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.login_page import LogPage
from source.time_track_pg import TimeTrack

def test_time_track(initialize_driver):

    try:

        driver = initialize_driver

        lp = LogPage(driver)
        lp.enter_username("admin")
        lp.enter_password("manager")
        lp.click_login_btn()

        tt = TimeTrack(driver)
        tt.click_time_track()

        wait_ = WebDriverWait(driver, 10)

        wait_.until(EC.title_is("actiTIME - View Time-Track"))

    except Exception as error_msg:
        td = datetime.now()
        screenshots_path = r"C:\Users\ASUS\PycharmProjects\framework_actitime\screenshots\\"
        name = f"screenshot-{td.day}-{td.month}-{td.year}-{td.hour}-{td.minute}-{td.second}.png"
        driver.save_screenshot(screenshots_path + name)
        raise error_msg
