# diploma_project
Дипломный проект по литературному порталу Author.Today.

Author.Today - литературный портал, где авторы сами публикуют свои произведения.
К сентябрю 2024 года на портале опубликовано более 190 000 книг.
Проект существует с 2016 года и позиционируется также как социальная сеть, в которой можно вести блог.
В 2019 году вышло приложение, которое согласно данным Google Play скачано более 100 000 раз.


## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/AnnaGarap/diploma_project'
2. Установить зависимости 'pip install -r requirements.txt'

3. Для API тестирования согласно информации из API документации проекта https://api.author.today/home/maininfo:
   - Необходимо пройти авторизацию, например, логин: anne.test3@yandex.ru, пароль: BooksLove, на сайте https://author.today/
   - Получить токен на странице https://author.today/account/bearer-token
   - Ввести полученный токен в переменную token в файле tests_api.py после Bearer.
4. Запустить тесты 'pytest'
5. Сгенерировать отчет 'allure generate allure-files -o allure-report'
6. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests

### Полезные ссылки
- API документация https://api.author.today/

### Струткура:
- ./test - тесты
- ./pages - описание страниц

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager 
- pip install allure-pytest