import allure
from locators.forgot_page_locators import ForgotPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPage(BasePage):

    @allure.step('Ожидаем загрузки страницы Восстановления пароля')
    def wait_for_forgot_page_loaded(self):
        self.wait_for_url(Urls.FORGOT_PAGE_URL)

    @allure.step('Заполняем поле "emai"')
    def fill_email_field(self, email):
        self.send_keys_to_place(ForgotPageLocators.EMAIL_FIELD, email)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_restore_button(self):
        self.click_element(ForgotPageLocators.RESTORE_BUTTON)