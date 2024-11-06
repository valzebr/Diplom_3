import allure
from urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

class TestProfilePage:

    @allure.title('Проверка перехода по кнопке "Личный кабинет" в профиль пользователя')
    def test_open_profile_page(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        login_page.open_page(Urls.LOGIN_PAGE_URL)
        login_page.fill_user_data_form(registered_user['email'], registered_user['password'])
        main_page.click_profile_link()
        user_name = profile_page.get_text_from_name_field()

        assert user_name == registered_user['name']

    @allure.title('Проверка перехода в раздел "История заказов"')
    def test_open_order_history(self, main_page, profile_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.click_profile_link()
        profile_page.click_order_history_link()
        assert profile_page.get_url() == Urls.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, main_page, profile_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.click_profile_link()
        profile_page.click_exit_button()
        profile_page.wait_for_login_page_loaded()
        assert profile_page.get_url() == Urls.LOGIN_PAGE_URL