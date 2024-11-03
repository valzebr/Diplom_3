import allure
import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import Urls, Api

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.forgot_page import ForgotPage
from pages.reset_page import ResetPage

@pytest.fixture(scope='function', params=['firefox', 'chrome'])
@allure.title('Запуск драйвера')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1024,1080')
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.title('Генерация данных пользователя')
@pytest.fixture(scope='function')
def generate_user():
    creds = generate_user_creds()
    return creds

@allure.title('Регистрация юзера')
@pytest.fixture(scope='function')
def registered_user(generate_user):
    response = requests.post(Api.register_api, data=generate_user)
    access_token = response.json()['accessToken']
    yield generate_user
    requests.delete(Api.user_api, headers={"Authorization": access_token})

fake = Faker("ru_RU")
@allure.title('Генерация данных пользователя')
def generate_user_creds():
    data = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    return data

@allure.title('Авторизация юзера')
@pytest.fixture(scope='function')
def authorize_user(driver, registered_user):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    driver.get(Urls.LOGIN_PAGE_URL)
    login_page.fill_user_data_form(registered_user['email'], registered_user['password'])
    main_page.wait_for_load_main_page()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture
def forgot_page(driver):
    return ForgotPage(driver)

@pytest.fixture
def reset_page(driver):
    return ResetPage(driver)