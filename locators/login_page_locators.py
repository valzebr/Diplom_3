from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL_AUTH_FIELD = By.XPATH, ".//*[text()='Email']/following-sibling::input"  # поле ввода email
    PASSWORD_FIELD = By.XPATH, ".//input[@type = 'password']"  # поле ввода пароля
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка "Войти"
    RESTORE_PASSWORD_LINK = By.LINK_TEXT, "Восстановить пароль" # ссылка Восстановить пароль