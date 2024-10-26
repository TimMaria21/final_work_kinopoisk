import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from page_ui import Ui
from config import url_ui, login, password


ui = Ui(url_ui)


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.step("Поиск фильма по названию.")
def test_search(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Закрыть рекламу.'):
        ui.advertising()
    with allure.step('Ввести в поисковик название фильма.'):
        movie = "Зеленая книга"
    ui.search(movie)
    ui.click_search_button()
    ui.first_on_the_list()
    with allure.step('Проверить, что полученные данные совпадают c названием фильма.'):
        assert movie in driver.title


@allure.step("Получение информации о персонаже")
def test_person(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Закрыть рекламу'):
        ui.advertising()
    with allure.step('Вводим ФИ персоны.'):
        person = "Вадик Королев"
    ui.search(person)
    ui.click_search_button()
    with allure.step('Проверить, что открылась страница персоны'):
        assert person in driver.title
    

@allure.step("Пустое значение в поисковой строке (поиск 'случайный фильм').")
def test_filter(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Закрыть рекламу.'):
        ui.advertising()
    with allure.step('Нажимаем на кнопку "СЛУЧАЙНЫЙ ФИЛЬМ".'):
        ui.click_search_button()
    ui.random_movie()
    with allure.step('Проверяем рандомный фильм.'):
        assert "" in driver.name


@allure.step("Фильтрация по стране, году и жанру.")
def test_filter_by_country(driver: WebDriver):
    driver.get(url_ui)
    ui=Ui(driver)
    with allure.step('Закрыть рекламу.'):
        ui.advertising()
    with allure.step('Нажать кноку фильтрации и ввести данные в поля "страна", "год", "жанр".'):
        ui.filtering()
    country = "Россия"
    year = "1993"
    genre ="комедия"
    ui.filter_by_country(country)
    ui.filter_year(year)
    ui.filter_by_genre(genre)
    ui.filter_search()
    ui.open_movie()
    with allure.step('Проверить совпадают ли полученные данные с веденными нами данными'):
        assert ui.filter_result_year() == year
        assert ui.filter_result_country() == country
        assert ui.filter_result_genre() == genre


@allure.step("Топ-250")
def test_top_250(driver: WebDriver):
    driver.get(url_ui)
    ui=Ui(driver)
    with allure.step('Закрыть рекламу'):
        ui.advertising()
    with allure.step('Проверить совпадает ли название "топа" с тем, что мы искали'):
        assert ui.top_250() == "250 лучших фильмов"


@allure.step("Частичная авторизация")
def test_authorization(driver: WebDriver):
    driver.get(url_ui)
    ui = Ui(driver)
    with allure.step('Закрыть рекламу'):
        ui.advertising()
    with allure.step('Ввести логин и пароль'):
        ui.authorization(login, password)
    with allure.step('Проверить на соответсвие ожидаемого текста'):
        assert ui.risk_hacking() == 'Введите символы с картинки'
    #дальше этого шага автоматизированную проверку авторизации у меня не получилось,
    #так как приложение запрашивает введение символов с картинки.