import allure
from urls import Urls


class TestMainFunctions:

    def open_main_page(self, main_page):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.wait_for_load_main_page()

    @allure.title('Проверка перехода на главную страницу по клику на кнопку "Конструктор"')
    def test_open_constructor(self, login_page, main_page):
        login_page.open_page(Urls.LOGIN_PAGE_URL)
        login_page.click_constructor_button()
        self.open_main_page(main_page)
        assert main_page.get_url() == Urls.MAIN_PAGE_URL

    @allure.title('Проверка перехода в Ленту заказов')
    def test_open_order_feed(self, main_page, feed_page):
        self.open_main_page(main_page)
        main_page.click_feed_button()
        assert feed_page.get_url() == Urls.FEED_PAGE_URL

    @allure.title('Проверка, что по клику на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_modal(self, main_page):
        self.open_main_page(main_page)
        main_page.click_on_ingredient()
        assert main_page.find_ingredient_modal()

    @allure.title('Проверка, что по клику на крестик всплывающее окно с деталями закрывается')
    def test_close_ingredient_modal(self, main_page):
        self.open_main_page(main_page)
        main_page.click_on_ingredient()
        main_page.close_ingredient_modal()
        assert not main_page.check_visibility_modal()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_added_ingredient_increased_counter(self, main_page):
        self.open_main_page(main_page)
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        assert main_page.get_actual_counter(ingredient) == main_page.expected_count(ingredient)

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_create_order_by_authorized_user(self, main_page, login_page, authorize_user):
        self.open_main_page(main_page)
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        assert main_page.find_order_modal()