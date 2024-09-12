import allure
import requests
import json

base_url = "https://api.author.today"
fio = 'Анна Г'
email = 'anne.test20@yandex.ru'
temp_email = 'jocalon919@kernuo.com'
password = 'BooksLove'
content_type = 'application/json'
token = 'Bearer 961_x6me3HesBggps_VMs6i-q1EpGxBiluV9YnJ6ZWsIV9qePPCT7Ot5NKO1woCzfOOrWwMcSoSqtIBGuqRKSM0J_putWUTQ2OsmJvBteu2HEJuCByaCUUHEA_jwnYrAlwoylayytryDArxc2D6aXY5ZwpW0paGogSgrXAkSmx6D47If8zzia3G4uSANtPIkeEsHJgb-3TprVI2TlPsRhugT3nvEHKaV7iQiLJbaGUKqF4tDWx3XcyVTO8g7mjYRPZIu2CJEXUggSA-BudMqFinJ9AtNC2NcU3XK49WXqCmZgt5XneZVWXZH2LRaPd5u5BOmytOB2yWI66pP3Zm7JqiysbD7oCgj4j054ukROOGvGrxlEaY-rVZv0u-IlzBuBEveGx6YZ6wTCqH_CkS3Lm5uYu6-fo8E5yJpEpkoUgKmPHLsl44A5_4fRZ4-gBGe1Jm5luJXdOMctrAvkfrFMomfFjBD8V5tuVHNAf7WY5BC6uSEi5ZkT_pIt6kua_Rj5-4Nr4Jpo7UrrZhrAJRCUxX6bqg0QebOhIet7oDQhbd7ApbVoPK3C1H_Fc0CE3j2b6yOv4F5yjPAQ-ct9Hlsjca5tMwYd5sq5Qh43x2Nqls_QEu2'
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
    payload = json.dumps = ({
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
