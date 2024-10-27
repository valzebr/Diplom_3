import allure
import pytest
import requests
from selenium import webdriver
from faker import Faker
from urls import URLS
from endpoints import Api
from pages.login_page import LoginPage
from pages.main_page import MainPage

fake = Faker("ru_RU")


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        browser = webdriver.Chrome(options=options)
    browser.get(URLS.MAIN_PAGE_URL)
    yield browser
    browser.quit()



@allure.title('Регистрация юзера')
@pytest.fixture(scope='function')
def registered_user(generate_user):
    response = requests.post(Api.register_api, data=generate_user)
    access_token = response.json()['accessToken']
    yield generate_user
    requests.delete(Api.user_api, headers={"Authorization": access_token})


def generate_user_creds():
    data = {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.name()
    }
    return data