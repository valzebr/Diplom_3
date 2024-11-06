import allure
from urls import Urls
from locators.reset_page_locators import ResetLocators
from pages.base_page import BasePage


class ResetPage(BasePage):

    @allure.step('Ожидаем загрузки страницы сброса пароля')
    def wait_for_reset_page_loaded(self):
        self.wait_for_url(Urls.RESET_PAGE_URL)

    @allure.step('Нажимаем на кнопку показа пароля')
    def click_on_show_password(self):
        self.click_element(ResetLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Получаем класс поля ввода пароля')
    def get_password_field_class(self):
        element_class = self.find_and_wait_element(ResetLocators.PASSWORD_FIELD).get_attribute('class')
        return element_class