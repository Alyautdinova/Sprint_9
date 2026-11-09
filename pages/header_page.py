from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):

    # метод нажатия на кнопку "Создать аккаунт"
    def click_create_account_button(self):
        self.click(HeaderLocators.create_account_button)

    # метод нажатия на кнопку "Войти"
    def click_sigin_button(self):
        self.click(HeaderLocators.sigin_button)
    