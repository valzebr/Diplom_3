from urls import URLS

class Api:
    register_api = URLS.MAIN_PAGE_URL + 'api/auth/register'
    user_api = URLS.MAIN_PAGE_URL + 'api/auth/user'
    login_api = URLS.MAIN_PAGE_URL + 'api/auth/user/login'