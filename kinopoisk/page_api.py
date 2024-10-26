import requests
from typing import Dict, Any, Tuple


class API:
    def __init__(self, url) -> None:
        self.url = url


    def get_movie_by_name(self, name_to_movie: str, headers: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск фильма или сериала по его названию.
        Args:
            name_to_movie (str): название фильма или сериала.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией о фильме/сериале и статус код.
        """
        result_get_movie_by_name = requests.get(
            self.url + "movie/search?query=" + name_to_movie, headers=headers
        )
        return result_get_movie_by_name.json(), result_get_movie_by_name.status_code


    def get_movie_by_id(self, id: int, headers: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск фильма или сериала по его id номеру.
        Args:
            id (int): id номер фильма или сериала.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией о фильме/сериале и статус код.
        """
        result_get_movie_by_id = requests.get(
            self.url + "movie/" + str(id), headers=headers
        )
        return result_get_movie_by_id.json(), result_get_movie_by_id.status_code


    def get_person_by_name(self, person_name: str, headers: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск персоны по имени.
        Args:
            person_name (str): имя + фамилия персоны.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией о персоне и статус код.
        """
        result_get_person_by_name = requests.get(
            self.url + "person/search?query=" + person_name, headers=headers
        )
        return result_get_person_by_name.json(), result_get_person_by_name.status_code


    def get_person_by_id(self, id: int, headers: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск актера/персоны по его id номеру.
        Args:
            id (int): id номер персоны.
        Returns:
            Tuple[Dict[str, Any], int]: json ответ с информацией о персоне и статус код.
        """
        result_get_person_by_id = requests.get(
            self.url + "person/" + str(id), headers=headers
        )
        return result_get_person_by_id.json(), result_get_person_by_id.status_code


    def get_movie_by_year_genre_country(self, year: int, genres_name: str, countries_name: str, headers: str) \
        -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск по определенной фильтрации.
        Получить список фильмов по году,типу жанра,стране производства.
        Args:
            genres.name, countries.name(str): жанр и страна,
            year(int): год выпуска.
        Returns:
            Tuple[List[Dict[str, str]], int]: json ответ с информацией по переданному значению и статус код.
        """
        params = {
            "year": year,
            "genres.name": genres_name,
            "countries.name": countries_name,
        }
        result_get_movie_by_year_genre_country = requests.get(
            self.url + "movie?", params=params, headers=headers
        )
        return result_get_movie_by_year_genre_country.json(), result_get_movie_by_year_genre_country.status_code
    

    def get_reward_person(self, person_id: str, headers: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет выполнить поиск наград.
        Негативная проверка. неправильное введение данных.
        "sortField и sortType должны быть одинаковой длины!"
            Tuple[List[Dict[str, str]], int]: json ответ с информацией по переданному значению и статус код.
        """
        params = {
            "page": 1,
            "limit": 10,
            "sortField": person_id,
        }
        result_get_reward_person = requests.get(
            self.url + "person/awards?", params=params, headers=headers
        )
        return result_get_reward_person.json(), result_get_reward_person.status_code