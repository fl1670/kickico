import time
import allure
from FW.BaseFW import BaseFW


class AnyPage(BaseFW):

    _button_Sign_In = '//*[@id="main-nav"]/ul[2]/li[5]/a/span'
    _button_profile = '//*[@id="main-nav"]/ul[2]/li[5]/button/img'
    _button_logout = '//*[@id="profile-nav-panel"]/div/a[5]'
    _iframe_launcher = '//*[@id="launcher"]'


    @allure.step('Нажимаем кнопку ВХОД')
    def click_button_Log_In(self):
        self.click_by_xpath(self._button_Sign_In)
        self.manager.waiting.waiting_for_the_element_to_be_clickable(self._iframe_launcher)
        return self.manager.sign_in

    @allure.step('Проверка ниличия кнопкb ВХОД')
    def check_button_Sign_In(self):
        return self.check_item(self._button_Sign_In)

    @allure.step('Нажимаем кнопку Профайл')
    def click_button_profile(self):
        self.click_by_xpath(self._button_profile)
        # задержка на анимацию
        time.sleep(0.5)
        return self

    @allure.step('Нажимаем кнопку Выход')
    def click_button_logout(self):
        self.click_by_xpath(self._button_logout)
        self.manager.waiting.waiting_for_the_element_to_be_clickable(self._iframe_launcher)
        return self




