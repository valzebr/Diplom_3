from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Получить текущий URL
    def get_url(self):
        return self.driver.current_url

    # открываем нужную страницу
    def open_page(self, url):
        self.driver.get(url)

    # Ожидание отображения локатора
    def find_and_wait_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    # Клик по кнопке
    def click_element(self, locator):
        self.find_and_wait_element(locator).click()

    # Заполнение формы
    def send_keys_to_place(self,locator,text):
        self.find_and_wait_element(locator).send_keys(text)

    # Получить текст элемента
    def get_text_locator(self, locator):
        return self.find_and_wait_element(locator).text

    # Скролл к нужному элементу
    def scroll_to_element(self, locator):
        element = self.find_and_wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Ожидаем нужный урл
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    # Проверяем видимость
    def check_visibility_of_element(self, locator):
        try:
            self.driver.find_and_wait_element(locator)
            return True
        finally:
            return False

    # ожидаем, пока элемент не исчез
    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(locator))

    # Перетаскивание
    def drag_n_drop(self, source, target):
        action_chains = ActionChains(self.driver)
        drag = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(source))
        drop = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(target))
        action_chains.drag_and_drop(drag, drop).perform()
