from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from Data.GroupData import group_data


class DriverInstance:

    driver = None

    def __init__(self):
        self.group_data = group_data

    def get_Driver_Instance(self):
        if self.driver is None:
            if self.group_data.GLOBAL['Browser']['Name'] == 'firefox':
                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4444/wd/hub',
                    browser_profile=None,
                    desired_capabilities=DesiredCapabilities.FIREFOX,
                    proxy=None,
                    keep_alive=False,
                    file_detector=None
                )
            if self.group_data.GLOBAL['Browser']['Name'] == 'chrome':
                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.CHROME,
                    browser_profile=None,
                    proxy=None,
                    keep_alive=False,
                    file_detector=None
                )
            if self.group_data.GLOBAL['Browser']['Name'] == 'internet explorer':
                self.driver = webdriver.Remote(
                    command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
                    browser_profile=None,
                    proxy=None,
                    keep_alive=False,
                    file_detector=None
                )
            self.driver.maximize_window()
        return self.driver

    def get_driver(self):
        if self.driver is None:
            self.get_Driver_Instance()
        return self.driver

    def stop_Test(self):
        if self.driver is not None:
            self.driver.quit()
