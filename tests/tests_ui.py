import allure
from conftest import driver
from pages.PagesForUI import Pages


@allure.story("Поиск. Валидные проверки")
@allure.title("Поиск книги по названию")
@allure.severity("critical")
def test_valid_search_book(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Поиск произведения, автора или запись в блоге"):
        pages.search("счастье")

#    with allure.step(""):
#        assert 


@allure.story("Поиск. Невалидные проверки")
@allure.title("Поиск книги по названию")
@allure.severity("critical")
def test_invalid_search_book(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Поиск произведения, автора или запись в блоге"):
        pages.search("fgjdfilojhsikushgzd")

#    with allure.step(""):
#        pages.search_result
#        assert "" in .... text("Ваш запрос не дал результатов.")
