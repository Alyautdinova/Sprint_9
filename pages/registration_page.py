from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators

class RegistrationPage(BasePage):

    # метод заполнения поля "Имя"
    def set_first_name(self, first_name):
        self.send_keys(RegistrationLocators.first_name_input, first_name)

    # метод заполнения поля "Фамилия"
    def set_last_name(self, last_name):
        self.send_keys(RegistrationLocators.last_name_input, last_name)

    # метод заполнения поля "Имя пользователя"
    def set_username(self, username):
        self.send_keys(RegistrationLocators.username_input, username)

    # метод заполнения поля "Адрес электронной почты"
    def set_email(self, email):
        self.send_keys(RegistrationLocators.email_input, email)

    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(RegistrationLocators.password_input, password)

    # метод нажатия на кнопку "Создать аккаунт"
    def click_create_account_button(self):
        self.click(RegistrationLocators.create_account_button)

    # метод создания аккаунта
    def create_account(self, first_name, last_name, username, email, password):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)
        self.click_create_account_button()
    