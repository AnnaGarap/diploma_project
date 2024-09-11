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

    def search(self, text: str):
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="icon-search"]').click()
        self._waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[name="q"]')))
        self._driver.find_element(
            By.CSS_SELECTOR, 'input[name="q"]').send_keys(text, Keys.RETURN)

# добавить ожидание пока откроется страница //*[@id="search-results"]/div[1]/div[1]/text()
#    def search_result(self):

    def open_list_of_all_books(self):
        self._driver.find_element(
            By.XPATH, '[href="/work/genre/all/ebook"]').click()
        # добавить ожидание пока откроется страница
        # self._waiter.until()

#    def choose_genre(self):
#        self._driver.
