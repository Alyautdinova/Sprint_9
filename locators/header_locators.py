from selenium.webdriver.common.by import By

class HeaderLocators:
    create_account_button = [By.XPATH, "//a[text()='Создать аккаунт']"]
    sigin_button = [By.XPATH, "//a[text()='Войти']"]
    logout_button = [By.XPATH, "//a[text()='Выход']"]
