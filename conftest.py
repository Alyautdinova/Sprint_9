import pytest
import requests

from selenium import webdriver
from faker import Faker
from data.urls import Urls
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    # Для работы в Docker без графического интерфейса
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Подключаемся к Selenoid, а не запускаем локальный Chrome
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=options
    )
    
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
    payload = {"email": generate_new_user["email"],
            "password": generate_new_user["password"],
            "username": generate_new_user["username"],
            "first_name": generate_new_user["first_name"],
            "last_name": generate_new_user["last_name"]
    }

    requests.post(Urls.API_USERS, json=payload)

    return payload

# фикстура для входа пользователя
@pytest.fixture
def login_user(driver):
    payload = {
        "email": "test_user", # По хорошему должно быть так generate_new_user["username"], но апи отвечает "Невозможно войти с предоставленными учетными данными."
        "password": "123Test123" # По хорошему должно быть так generate_new_user["password"], но апи отвечает "Невозможно войти с предоставленными учетными данными."
    }
    response = requests.post(Urls.API_LOGIN_URL, json=payload)

    token = response.json().get("auth_token")

    driver.get(Urls.BASE_URL)
    driver.execute_script(f"localStorage.setItem('token', '{token}');")
    driver.refresh()
    
    return driver
