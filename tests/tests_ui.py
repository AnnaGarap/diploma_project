import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from pages.MainPage import MainPage

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
waiter = WebDriverWait(browser, 40)


@allure.id("AT-6")
@allure.story("Поиск. Валидные проверки")
@allure.title("Поиск книги по названию")
@allure.severity("critical")
def test_search_book(driver):
    with allure.step("Открыть сайт Author.Today"):
        main_page = MainPage(driver)
    with allure.step("Найти произведение, автора или запись в блоге"):
        main_page.search("счастье")


test_search_book()
