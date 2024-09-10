import allure
import requests
import json

base_url = "https://api.author.today"
fio = 'Анна Г'
email = 'anne.test20@yandex.ru'
temp_email = 'jocalon919@kernuo.com'
password = 'BooksLove'
content_type = 'application/json'
token = 'Bearer 7Efrb8hpAfjSclfXWFLSv4kT27_GNgJjTS-usMHY9wsxVmmEdPdH_tnFf-U0VPHbCOZrOGn8eTbKSNzq2mLeDFiWy18F8oWfzOgxs2dksIYzI4d2hDoKOTpqat7LcODebYyikJOzAadnS25yO1jcPOubcxDHgje1a5fnMIw4fyDIz5kDm539Llv4LhkDaflfFAC2F0xibxR7YvMpWS-Tn12stxw_-xhvrnV-lfCzzZsmEp_H6KflnYDjgEoAcPYwygxdxkFzVmqGt9AKs2SaT4v2DOqz4PUb5_nkDVegq0EEdHRC3L-HoAmotsH_xo2fX_O1It4HaeHul-WFyG_fDsdUE3ItMyVcMdmdYqHywH75WouXaUk10XamUmWl1Z2asNc4FRU7jHo0w_srYanBJohqtOlkY3JOiajFIrqX_woMR7Lol5OBecCiJwqUCYK5gzmfhWR1VRcDLkah61PrhltZ-uY-veoApVTCZdzWt9bZSbeewKx738Ows9MnAyRaQ8AopeqY9z6QKH9Y7Fop2do30eVAyPYTl5vL5hWIrjFKDyYN2jIr_JTxp5SHOoy-UrbM9tYW9zcWdEdBjT2HpYxTlVTCWxC0RnEmcn6cIF3G1bXG'
login = 'anne.test3@yandex.ru'


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
