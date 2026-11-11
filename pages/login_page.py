from pages.base_page import BasePage
from locators.login_locators import LoginLocatos

class LoginPage(BasePage):

    # метод заполнения поля email
    def set_username(self, username):
        self.send_keys(LoginLocatos.username_input, username)

    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(LoginLocatos.password_input, password)

    # метод нажатия на кнопку "Войти"
    def click_signin_button(self):
        self.click(LoginLocatos.signin_button)

    # метод входа
    def signin(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_signin_button()

    # метод для получения текстового значения заголовка страницы входа
    def get_login_header(self):
        return self.get_text(LoginLocatos.header)
    