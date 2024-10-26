import allure
from page_api import API
from config import url_api, headers

api = API(url_api)


@allure.feature("Поиск фильма/сериала.")
@allure.title("Тест на получение фильма/сериала по названию.")
def test_get_movie_by_name():
    with allure.step('Получить список с названием "Человек из Подольска"'):
        movie_name = "Человек из Подольска"
    result_get_movie_by_name, status_code = api.get_movie_by_name(movie_name, headers)
    with allure.step('Статус код = 200'):
        assert status_code == 200
    with allure.step('Проверить, что полученные данные совпадают c названием фильма'):
        assert result_get_movie_by_name["docs"][0]["name"] == movie_name


@allure.feature("Поиск фильма/сериала.")
@allure.title("Тест на получение информации о фильме/сериале по ID.")
def test_get_movie_by_id():
    with allure.step('Получить фильм, id которого = 456'):
        film_id = 456
    result_get_movie_by_id, status_code = api.get_movie_by_id(film_id, headers)
    with allure.step('Статус код = 200'):
        assert status_code == 200
    with allure.step('Проверить, что полученные данные совпадают c названием фильма'):
        assert result_get_movie_by_id["name"] == "Унесённые ветром"


@allure.feature("Поиск персоны.")
@allure.title("Тест на получение информации о персоне по имении и фамилии.")
def test_get_person_by_name():
    with allure.step('Найти персону с определенными именем и фамилией'):
        person_name = "Натали Портман"
    result_get_person_by_name, status_code = api.get_person_by_name(person_name, headers)
    with allure.step('Статус код = 200'):
        assert status_code == 200
    with allure.step('Проверить, что полученные данные совпадают c ФИ персоны'):
        assert result_get_person_by_name["docs"][0]["name"] == person_name



@allure.feature("Поиск персоны.")
@allure.title("Тест на получение информации о персоне по его ID на кинопоиске.")
def test_get_person_by_id():
    with allure.step('Ввести ID персоны'):
        person_id = 5661548
    result_get_person_by_id, status_code = api.get_person_by_id(person_id, headers)
    with allure.step('Статус код = 200'):
        assert status_code == 200
    with allure.step('Проверить, что полученные данные совпадают c ожидаемыми результатами'):
        assert result_get_person_by_id["name"] == "Вадик Королев"



@allure.feature("Поиск фильма.")
@allure.title("Тест на поиск фильма по фильтрации:год, жанр, страна.")
def test_get_movie_by_year_genre_country():
    with allure.step('Выставить фильтрацию по году, жанру и стране'):
        year = 1934
    genres_name = "ужасы"
    countries_name = "Мексика"
    result_get_movie_by_year_genre_country, status_code = api.get_movie_by_year_genre_country(
        year, genres_name, countries_name, headers
        )
    with allure.step('Статус код = 200'):
        assert status_code == 200
    with allure.step('Проверить, что полученные данные совпадают c ожидаемыми результатами'):
        assert result_get_movie_by_year_genre_country["docs"][0]["name"] == "Призрак монастыря"


@allure.feature("Поиск наград")
@allure.title("Негативная проверка. Тест на получение инофрмации о наградах(неправильное введение данных)")
def test_get_reward_person():
    person_id = "personId"
    result_get_reward_person, status_code = api.get_reward_person(person_id, headers)
    with allure.step('Статус код = 400'):
        assert status_code == 400
    with allure.step("sortField и sortType должны быть одинаковой длины!"):
        assert result_get_reward_person ["error"] == "Bad Request"