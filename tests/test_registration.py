import allure

from pages.header_page import HeaderPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from data.urls import Urls

class TestRegistration:
    def test_registration(self, driver, generate_new_user):
        headerPage = HeaderPage(driver)
        headerPage.open(Urls.BASE_URL)
        headerPage.click_create_account_button()

        registrationPage = RegistrationPage(driver)
        assert registrationPage.get_current_url() == Urls.REGISTRATION_URL

        registrationPage.create_account(first_name=generate_new_user["first_name"],
                                        last_name=generate_new_user["last_name"],
                                        username=generate_new_user["username"],
                                        email=generate_new_user["email"],
                                        password=generate_new_user["password"])

        loginPage = LoginPage(driver)
        assert loginPage.is_current_url(Urls.LOGIN_URL)
        assert loginPage.get_login_header() ==  "Войти на сайт"
