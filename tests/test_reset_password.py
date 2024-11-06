import allure
from urls import Urls


class TestResetPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_forgot_page(self, login_page, forgot_page):
        login_page.open_page(Urls.LOGIN_PAGE_URL)
        login_page.click_restore_password()
        forgot_page.wait_for_forgot_page_loaded()
        assert forgot_page.get_url() == Urls.FORGOT_PAGE_URL

    @allure.title('Проверка переход на страницу сброса пароля по кнопке «Восстановить»')
    def test_open_reset_page(self, forgot_page, reset_page):
        forgot_page.open_page(Urls.FORGOT_PAGE_URL)
        forgot_page.fill_email_field('test@email.ru')
        forgot_page.click_restore_button()
        reset_page.wait_for_reset_page_loaded()
        assert reset_page.get_url() == Urls.RESET_PAGE_URL

    @allure.title('Проверка что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_password(self, forgot_page, reset_page):
        forgot_page.open_page(Urls.FORGOT_PAGE_URL)
        forgot_page.fill_email_field('test@email.ru')
        forgot_page.click_restore_button()
        reset_page.wait_for_reset_page_loaded()
        reset_page.click_on_show_password()
        assert 'input_status_active' in reset_page.get_password_field_class()