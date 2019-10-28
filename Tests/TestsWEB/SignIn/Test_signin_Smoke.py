import time

import allure
import pytest

from Tests.TestBase import TestBase


@allure.testcase('https://yandex.ru/search/?text=%D0%B3%D0%B4%D0%B5%20%D1%82%D0%BE%20%D1%82%D1%83%D1%82%20%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D0%BC%20%D1%82%D0%B5%D1%81%D1%82%D1%8B&lr=47')
@allure.feature('Web')
@allure.story('Проверка авторизации пользователя')
class Test_signIn_smoke(TestBase):

    Log_Pas = [{'flex-nn@yandex.ru', 'qwerty'},
               {'Fail', 'Fail'}]

    @allure.title('Тест 1 - Валидный вход')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.signin
    @pytest.mark.parametrize("Login, Password", Log_Pas)
    def test_1_sign_in_smoke(self, Login, Password):
        self.any_page.click_button_Log_In()
        self.APP.sign_in.set_username(Login)
        self.APP.sign_in.set_password(Password)
        self.APP.sign_in.click_button_sign_in()
        assert False == self.APP.main_page.check_button_Sign_In()

    @allure.title('Тест 2 - Не коректный логин')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.signin
    def test_2_sign_in_smoke(self):
        self.any_page.click_button_Log_In()
        self.APP.sign_in.set_username('Test')
        self.APP.sign_in.set_password('Password')
        self.APP.sign_in.click_button_sign_in()

        assert 'Password or email is incorrect.' in self.APP.sign_in.get_text_danger_login()

    @allure.title('Тест 3 - Пустое поле пароль')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.signin
    def test_3_sign_in_smoke(self):
        self.any_page.click_button_Log_In()
        self.APP.sign_in.set_username('flex-nn@yandex.ru')
        self.APP.sign_in.click_button_sign_in()

        assert 'Необходимо заполнить поле «Пароль».' in self.APP.sign_in.get_text_danger_password()



