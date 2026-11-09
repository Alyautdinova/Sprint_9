import pytest

from selenium import webdriver
from faker import Faker

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    driver.quit()

# фикстура для создания пользователя
@pytest.fixture
def generate_new_user():

    fake = Faker()

    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name + "_" + last_name
    email = fake.email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    
    # собираем тело запроса
    user = {
        "first_name":first_name,
        "last_name":last_name,
        "username":username,
        "email": email,
        "password": password
        }
    
    return user