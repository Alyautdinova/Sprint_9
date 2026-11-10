from selenium.webdriver.common.by import By

class LoginLocatos:
    username_input = [By.NAME, "email"]
    password_input = [By.NAME,"password"]
    signin_button = [By.XPATH, "//button[text()='Войти']"]
    header = [By.XPATH, "//h1"]
    