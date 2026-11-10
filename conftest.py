import pytest

from selenium import webdriver
from faker import Faker
from data.urls import Urls
from pages.header_page import HeaderPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()

# фикстура для генерации пользователя
@pytest.fixture
def generate_new_user():

    fake = Faker()

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + "_" + last_name
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "username":username,
        "email": email,
        "password": password
        }
    
    return user

# фикстура для создания пользователя
@pytest.fixture
def register_new_user(generate_new_user, driver):
    headerPage = HeaderPage(driver)
    headerPage.open(Urls.BASE_URL)
    headerPage.click_create_account_button()

    registrationPage = RegistrationPage(driver)
    registrationPage.create_account(first_name=generate_new_user["first_name"],
                                    last_name=generate_new_user["last_name"],
                                    username=generate_new_user["username"],
                                    email=generate_new_user["email"],
                                    password=generate_new_user["password"])

    return {
        "username": generate_new_user["username"],
        "password": generate_new_user["password"]
    }
