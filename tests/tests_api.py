import allure
import requests
import json

base_url = "https://api.author.today"
fio = 'Анна Г'
email = 'anne.test20@yandex.ru'
temp_email = 'jocalon919@kernuo.com'
password = 'BooksLove'
content_type = 'application/json'
token = 'Bearer WnmBg3YLOve1iVH2FC-8EY-My9MxQOr-z-nkVlEFocBd4PhF6IV1Sk-dUOk6MMuNgA9pLpfcQejLkjVYKLc972CEA9OxRAHOKs_2XIbtdnorP9P987hgnHBMsZIjBTY6UpYgIxsmI8zAw3KKz6j0k5zPdsoFv_LLkA1wzQe3eFXpuM70cls1RuBPIpQqJAj8gkJOx23PpyHcABCSJxd9Y0TB_UdmxXnsK_3xoMBk9n5tCvK4u6DJE7-gJkY2ZMHKxJDmNlkTpyUGUgWPZxJzvd5RmlhiK3CRVOKgJOk7dBAV0188MG4zIKINalgA8LylyhTbf9VnbBld8kTPcWp09q8Z_t-Hb2P2n5stbr0rrpz3kHzx3X03vd81CMgDb-h_1xYMj2c5nKHlnv6AVaplaY5EAw6BnaM3YuL3w9l1JvU5YYybklIIMwk1xKkSD2ESJx6p4n54O0Opfz7AqjzMAQIH-lU1m3w5YW6eMzq00_Rcu_fkCi2zelQWZecjCZIHctK4em_DqfxIVjX8g41fSBD0FOkd1cCeW29kBThIRQAmxhw2Vbizv7PYNrV2XbUWCfG4iVE3xyby7o5tsS33ILafHDhuvryq7H9_JYZGknFgiNzo'
login = 'anne.test3@yandex.ru'


@allure.id("AT-1")
@allure.story("Регистрация. Невалидные проверки")
@allure.title("Регистрация с пустым ФИО")
@allure.severity("critical")
def test_api_register_empty_fio():
    payload = json.dumps = ({
        'fio': '',
        'email': email,
        'password': password,
    })
    headers_info = {
        'Content-Type': content_type,
        'Authorization': token
    }
    response = requests.post(
        base_url+"/v1/account/register", headers=headers_info,
        data=payload)
    assert response.status_code == 403
    print(response.status_code, response.text)


@allure.id("AT-2")
@allure.story("Регистрация. Невалидные проверки")
@allure.title("Регистрация с временной почтой")
@allure.severity("critical")
def test_api_register_temp_email():
    payload = json.dumps = ({
        'fio': fio,
        'email': temp_email,
        'password': password,
    })
    headers_info = {
        'Content-Type': content_type,
        'Authorization': token
    }
    response = requests.post(
        base_url+"/v1/account/register", headers=headers_info,
        data=payload)
    assert response.status_code == 403
    print(response.status_code, response.text)


@allure.id("AT-3")
@allure.story("Регистрация. Невалидные проверки")
@allure.title("Регистрация с пустым Email")
@allure.severity("critical")
def test_api_register_empty_email():
    payload = json.dumps = ({
        'fio': fio,
        'email': '',
        'password': password,
    })
    headers_info = {
        'Content-Type': content_type,
        'Authorization': token
    }
    response = requests.post(
        base_url+"/v1/account/register", headers=headers_info,
        data=payload)
    assert response.status_code == 403
    print(response.status_code, response.text)


@allure.id("AT-4")
@allure.story("Регистрация. Невалидные проверки")
@allure.title("Регистрация с пустым паролем")
@allure.severity("critical")
def test_api_register_empty_password():
    payload = json.dumps = ({
        'fio': fio,
        'email': email,
        'password': '',
    })
    headers_info = {
        'Content-Type': content_type,
        'Authorization': token
    }
    response = requests.post(
        base_url+"/v1/account/register", headers=headers_info,
        data=payload)
    assert response.status_code == 403
    print(response.status_code, response.text)


@allure.id("AT-5")
@allure.story("Авторизация. Валидные проверки")
@allure.title("Авторизация пользователя")
@allure.severity("critical")
def test_api_auth():
    payload = json.dumps({
        "Login": login,
        "Password": password,
        "Code": ""
    })
    headers_info = {
        'Content-Type': content_type,
        'Authorization': token
    }
    response = requests.post(
        base_url+"/v1/account/login-by-password", headers=headers_info,
        data=payload)
    assert response.status_code == 200
    print(response.status_code, response.text)


test_api_register_empty_fio()
test_api_register_temp_email()
test_api_register_empty_email()
test_api_register_empty_password()
test_api_auth()
