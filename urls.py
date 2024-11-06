class Urls:

    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'  # URL главной страницы
    FEED_PAGE_URL = f"{MAIN_PAGE_URL}/feed" # URL ленты заказов
    LOGIN_PAGE_URL = f'{MAIN_PAGE_URL}/login'  # URL страницы авторизации
    REG_PAGE_URL = f'{MAIN_PAGE_URL}/register'  # URL страницы регистрации
    FORGOT_PAGE_URL = f'{MAIN_PAGE_URL}/forgot-password'  # URL страницы восстановления пароля
    RESET_PAGE_URL = f'{MAIN_PAGE_URL}/reset-password'  # URL страницы сброса пароля
    PROFILE_PAGE_URL = f'{MAIN_PAGE_URL}/account/profile'  # URL личный кабинет\профиля
    ORDER_HISTORY_URL = f'{MAIN_PAGE_URL}/account/order-history'  # URL личный кабинет\истории заказов

class Api:
    register_api = Urls.MAIN_PAGE_URL + 'api/auth/register'
    user_api = Urls.MAIN_PAGE_URL + 'api/auth/user'
    login_api = Urls.MAIN_PAGE_URL + 'api/auth/user/login'