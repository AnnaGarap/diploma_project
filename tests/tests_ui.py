import allure
from selenium.webdriver.common.by import By
from pages.PagesForUI import Pages


@allure.story("Поиск. Валидные проверки")
@allure.title("Поиск книги по названию")
@allure.severity("critical")
def test_valid_search_book(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Ввод теста для поиска произведения"):
        pages.search("счастье")

    with allure.step("Проверить результат поиска"):
        text_of_button_show_all = driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/a[1]').text
        assert "показать все" in text_of_button_show_all, 'Текст не найден'


@allure.story("Поиск. Невалидные проверки")
@allure.title("Поиск книги по названию")
@allure.severity("critical")
def test_invalid_search_book(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Ввод теста для поска произведения"):
        pages.search("fgjdfilojhsikushgzd")

    with allure.step("Проверить результат поиска"):
        result_text = driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]').text
        assert "Ваш запрос не дал результатов." in result_text, 'Текст не найден'

@allure.story("Чтение книги")
@allure.title("Чтение фрагмента книги в ридере")
@allure.severity("critical")
def test_book_read(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Кликнуть на название книги"):
        pages.open_book()

    with allure.step("Кликнуть на кнопку Читать фрагмент"):
        pages.read_fragment()

    with allure.step("Проверить, что высвечивается кнопка Оглавление"):
        text_of_button_table_of_contents = driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/section[1]/header[1]/nav[1]/div[1]/button[1]/span[1]').text
        assert "Оглавление" in text_of_button_table_of_contents, 'Текст не найден'

@allure.story("Моя библиотека. Невалидные проверки")
@allure.title("Моя библиотека, если пользователь не авторизован")
@allure.description("Проверка открытия окна входа на сайт на странице Моя библиотека, если пользователь не авторизован")
@allure.severity("critical")
def test_my_library_invalid(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Выбрать меню Моя библиотека"):
        pages.open_my_books()

    with allure.step("Проверка наличия надписи Войти на сайт"):
        txt = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]').text
        assert "Войти на сайт" in txt, 'Текст не найден'

@allure.story("Страница все книги. Валидные проверки")
@allure.title("Сортировка списка книг по новизне")
@allure.severity("critical")
def test_filter_books(driver):
    with allure.step("Открыть сайт Author.Today"):
        pages = Pages(driver)

    with allure.step("Кликнуть на меню Книги"):
        pages.open_books()

    with allure.step("В меню Книги выбрать Все книги"):
        pages.open_list_of_all_books()

    with allure.step("Отсортировать список всех книг по новизне"):
        pages.sorting_by_novelty()

    with allure.step("Проверка наличия надписи "):
        text_of_header = driver.find_element(
            By.XPATH, '/html[1]/body[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]').text
        assert "Новинки книг" in text_of_header, 'Текст не найден'
