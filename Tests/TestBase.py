from FW.Application_Manager import Application_Manager
from Data.GroupData import group_data


class TestBase:
    APP = None
    GroupData = None
    main_page = None

    def setup_class(self):
        self.APP = Application_Manager()
        self.GroupData = group_data()
        self.any_page = self.APP.any_page.first_start()

    def teardown_class(self):
        self.APP.driver_instance.stop_Test()

    def setup_method(self):
        self.any_page.open_main_page(self.GroupData.GLOBAL[self.GroupData.branch]['main_page'])

    def teardown_method(self):
        if self.APP.main_page.check_button_Sign_In() is False:
            self.APP.main_page.click_button_profile()
            self.APP.main_page.click_button_logout()
