import allure
from locators.login_page_locators import LoginLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Заполняем поле "email"')
    def fill_email_field(self, email):
        self.send_keys_to_place(LoginLocators.EMAIL_AUTH_FIELD, email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_password_field(self, password):
        self.send_keys_to_place(LoginLocators.PASSWORD_FIELD, password)

    @allure.step('Заполняем форму авторизации пользователя')
    def fill_user_data_form(self, email, password):
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_element(LoginLocators.LOGIN_BUTTON)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def click_restore_password(self):
        self.click_element(LoginLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Кликаем по кнопке "Констурктор"')
    def click_constructor_button(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)