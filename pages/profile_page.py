import allure
from urls import Urls
from locators.profile_page_locators import ProfileLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Получаем текст из поля "Имя"')
    def get_text_from_name_field(self):
        name = self.find_and_wait_element(ProfileLocators.NAME_FIELD).get_property('value')
        return name

    @allure.step('Нажимаем на ссылку "История заказов"')
    def click_order_history_link(self):
        self.find_and_wait_element(ProfileLocators.ORDER_HISTORY).click()

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_exit_button(self):
        self.click_element(ProfileLocators.EXIT_BUTTON)

    @allure.step('Ожидаем загрузки страницы авторизации')
    def wait_for_login_page_loaded(self):
        self.wait_for_url(Urls.LOGIN_PAGE_URL)

    def get_user_order(self):
        element = self.find_and_wait_element(ProfileLocators.ORDER_NUMBER)
        return element.text