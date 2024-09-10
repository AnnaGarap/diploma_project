# diploma_project
Дипломный проект



Для API тестирования согласно информации из документации https://api.author.today/home/maininfo:
1. Необходимо пройти авторизацию на сайте https://author.today/
2. Получить токен на странице https://author.today/account/bearer-token
3. Ввести полученный токен в переменную token в файле tests_ui.py после Bearer.

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone https://github.com/AnnaGarap/diploma_project'
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

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
- pyp install pytest
- pip install selenium
- pip install webdriver-manager 
- pip install allure-pytest