from selenium.webdriver.common.by import By

class LoginLocatos:
    email_input = [By.NAME, "email"]
    password_input = [By.NAME,"password"]
    signin_button = [By.XPATH, "//button[text()='Войти']"]
    