from pages.base_page import BasePage
from locators.login_locators import LoginLocatos

class LoginPage(BasePage):

    # метод заполнения поля "Пароль"
    def set_password(self, password):
        self.send_keys(LoginLocatos.password_input, password)

    # метод нажатия на кнопку "Войти"
    def click_signin_buuton(self):
        self.click(LoginLocatos.signin_buuton)

    # метод входа
    def signin(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_signin_buuton()
    