from selenium.webdriver.common.by import By


class RecoveryLocators:
    PASSWORD_FIELD = By.XPATH, "//label[text()='Пароль']/parent::div" # Поле ввода нового пароля
    SHOW_PASSWORD_BUTTON = By.XPATH, ".//div[contains(@class, 'input__icon')]" #Символ глаза пароля