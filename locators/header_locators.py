from selenium.webdriver.common.by import By


class HeaderLocators:

    CONSTRUCTOR_BUTTON = By.LINK_TEXT, "Конструктор"  # кнопка "Конструктор"
    FEED_BUTTON = By.XPATH, ".//p[text()='Лента Заказов']" #кнопка "Лента заказов"
    PROFILE_LINK = By.LINK_TEXT, "Личный Кабинет" #кнопка "Личный кабинет"