import allure

from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from data.urls import Urls

class TestLogin:

    @allure.title('Вход в аккаунт')
    @allure.description('Проверяем, что можем войти в аккаунт с корректными username и пароль')
    def test_login(self, register_new_user, driver):

        with allure.step('Подготовка данных для входа'):
            username = register_new_user["username"]
            password = register_new_user["password"]

        with allure.step('Открытие главной страницы'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)

        with allure.step('Нажатие на кнопку "Войти" в хедере'):
            headerPage.click_sigin_button()

        with allure.step('Проверка редиректа на страницу логина'):
            loginPage = LoginPage(driver)
            assert loginPage.get_current_url() == Urls.LOGIN_URL

        with allure.step('Логин'):
            loginPage.signin(username=username, password=password)

        with allure.step('Проверка редиректа на страницу Рецепты'):
            assert loginPage.is_current_url(Urls.RECIPES_URL)

        with allure.step('Проверка отображения кнопки "Выход"'):
            assert headerPage.is_visible_logout_button()
