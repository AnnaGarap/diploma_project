from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://author.today/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

# Надо задать явные ожидания:
# 1. появления поля ввода после клика на иконку с лупой.
# 2. появления результатов поиска
# И вероятно неправильный локатор поисковой строки
    def search(self, text: str):
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="icon-search"]').click()

        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="q"]').send_keys(
                text).sendKeys(Keys.RETURN)
