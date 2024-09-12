from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Pages:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.get("https://author.today/")
        self._waiter = WebDriverWait(driver, 10)

# Главная страница
    def search(self, text: str):
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="icon-search"]').click()
        self._waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[name="q"]')))
        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="q"]').send_keys(text, Keys.RETURN)

    def open_book(self):
        self._driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[2]/h4[1]/a[1]').click()

    def open_my_books(self):
        self._driver.find_element(
            By.XPATH, "//a[contains(text(),'Моя библиотека')]").click()

    def open_books(self):
        self._driver.find_element(By.XPATH, "//a[contains(text(),'Книги')]").click()

    def open_list_of_all_books(self):
        self._driver.find_element(
            By.XPATH, "/html[1]/body[1]/header[1]/div[1]/nav[1]/div[2]/ul[1]/li[1]/div[1]/div[1]/div[1]/ul[1]/li[4]/a[1]/span[1]").click()

# Страница книги
    def read_fragment(self):
        self._driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]').click()

# Страница все книги
    def sorting_by_novelty(self):
        self._driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]').click()
        self._driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]').click()
