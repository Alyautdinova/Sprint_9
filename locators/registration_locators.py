from selenium.webdriver.common.by import By

class RegistrationLocators:
    first_name_input = [By.NAME, "first_name"]
    last_name_input = [By.NAME, "last_name"]
    username_input = [By.NAME, "username"]
    email_input = [By.NAME, "email"]
    password_input = [By.NAME,"password"]
    create_account_button = [By.XPATH, "//button[text()='Создать аккаунт']"]
    