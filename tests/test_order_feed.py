import allure
from urls import Urls


class TestOrderFeed:

    @allure.title('Проверка открытия окна детализации заказа')
    def test_open_order_modal(self, feed_page):
        feed_page.open_page(Urls.FEED_PAGE_URL)
        feed_page.wait_for_load_feed_page()
        feed_page.click_first_feed_order()
        element = feed_page.find_order_modal()

        assert element

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_in_feed(self, main_page, feed_page, profile_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()
        main_page.click_profile_link()

        profile_page.click_order_history_link()
        user_order_from_history = profile_page.get_user_order()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        user_order_from_feed = feed_page.get_order()

        assert user_order_from_history in user_order_from_feed

    @allure.title('Увеличение счетчика заказов за все время')
    def test_order_counter_all_time_increased(self, main_page, login_page, feed_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.wait_for_load_main_page()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_before = feed_page.get_count_of_orders_all_time()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_after = feed_page.get_count_of_orders_all_time()

        assert count_after == count_before + 1

    @allure.title('Увеличение счетчика заказов за день')
    def test_order_counter_by_day_increased(self, main_page, login_page, feed_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.wait_for_load_main_page()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_before = feed_page.get_count_of_orders_by_day()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        count_after = feed_page.get_count_of_orders_by_day()

        assert count_after == count_before + 1

    @allure.title('Отображение созданного заказа "В работе"')
    def test_created_order_in_work_list(self, main_page, login_page, feed_page, authorize_user):
        main_page.open_page(Urls.MAIN_PAGE_URL)
        main_page.wait_for_load_main_page()

        login_page.click_constructor_button()
        main_page.wait_for_load_main_page()
        ingredient = main_page.choose_ingredient()
        main_page.add_ingredient(ingredient)
        main_page.click_order_button()
        main_page.wait_create_order()
        new_order = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.click_feed_button()
        feed_page.wait_for_load_feed_page()
        order_in_work = feed_page.get_order_in_work()

        assert new_order in order_in_work