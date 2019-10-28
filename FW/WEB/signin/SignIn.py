import allure
from FW.WEB.MainPage import MainPage


class SignIn(MainPage):

    _UserLogin_username = '//*[@id="UserLogin_username"][@type="text"]'
    _UserLogin_password = '//*[@id="UserLogin_password"][@type="password"]'
    _Sign_In = '//*[@id="login-form"]/div/input[@type="submit"]'
    _Forgot_password = '//*[@id="login-form"]/div[3]/p/a'
    _text_danger_login = '//*[@id="UserLogin_username"]/../small'
    _text_danger_password = '//*[@id="UserLogin_password"]/../small'

    @allure.step('Вводим Адрес электронной почты')
    def set_username(self, Login):
        self.send_keys_by_xpath(self._UserLogin_username, Login)
        return self

    @allure.step('Вводим Пароль')
    def set_password(self, password):
        self.send_keys_by_xpath(self._UserLogin_password, password)
        return self

    @allure.step('нажимаем кнопку Вход')
    def click_button_sign_in(self):
        self.click_by_xpath(self._Sign_In)
        return self.manager.main_page

    @allure.step('нажимаем "Забыли пароль?"')
    def click_Forgot_password(self):
        self.click_by_xpath(self._Forgot_password)
        return self.manager.recovery

    @allure.step('Получение текста предупреждения (login)')
    def get_text_danger_login(self):
        return self.get_tag_text(self._text_danger_login)

    @allure.step('Получение текста предупреждения (password)')
    def get_text_danger_password(self):
        return self.get_tag_text(self._text_danger_password)

