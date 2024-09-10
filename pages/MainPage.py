from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get("https://author.today/")

    def search(self, text: str):
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="icon-search"]').click()
        (WebDriverWait(self._driver, 10).
            until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="q"]'))))
        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="q"]').send_keys(text, Keys.RETURN)


# Надо задать явные ожидания:
# 1. появления поля ввода после клика на иконку с лупой.
# 2. появления результатов поиска
# И вероятно неправильный локатор поисковой строки
