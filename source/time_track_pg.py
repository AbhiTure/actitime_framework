import time

class TimeTrack:

    def __init__(self, driver):
        self.driver = driver

    def click_time_track(self):
        """clicking on view time track """
        self.driver.find_element("link text", 'View Time-Track').click()
        time.sleep(2)

