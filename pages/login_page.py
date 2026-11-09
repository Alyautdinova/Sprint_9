from pages.base_page import BasePage
from locators.login_locators import LoginLocatos

class LoginPage(BasePage):

    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(LoginLocatos.password_input, password)

    # метод нажатия на кнопку "Войти"
    def click_signin_button(self):
        self.click(LoginLocatos.signin_buuton)

    # метод входа
    def signin(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_signin_button()

    # метод для получения текстового значения заголовка страницы входа
    def get_login_header(self):
        return self.get_text(LoginLocatos.header)
    