import allure

from pages.header_page import HeaderPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from data.urls import Urls

class TestRegistration:

    @allure.title('Создание аккаунта')
    @allure.description('Проверяем, что можем создать аккаунт с корректным вводом всех полей')
    def test_registration(self, driver, generate_new_user):

        with allure.step('Открытие главной страницы'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)

        with allure.step('Нажатие на кнопку "Создать аккаунт" в хедере'):
            headerPage.click_create_account_button()

        with allure.step('Проверка редиректа на страницу регистрации'):
            registrationPage = RegistrationPage(driver)
            assert registrationPage.get_current_url() == Urls.REGISTRATION_URL

        with allure.step('Создание аккаунта'):
            registrationPage.create_account(first_name=generate_new_user["first_name"],
                                        last_name=generate_new_user["last_name"],
                                        username=generate_new_user["username"],
                                        email=generate_new_user["email"],
                                        password=generate_new_user["password"])

        with allure.step('Проверка редиректа на страницу логина'):
            loginPage = LoginPage(driver)
            assert loginPage.is_current_url(Urls.LOGIN_URL)

        with allure.step('Проверка заголовка страницы логина'):
            assert loginPage.get_login_header() ==  "Войти на сайт"
