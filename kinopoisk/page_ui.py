import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC


class Ui():
   
    def __init__(self, url) -> None:
        self.url = url


    @allure.step("Введение в поисковик ФИ персонажа.")
    def search(self, person: str) -> None:
        self.url.find_element(By.CSS_SELECTOR, "input[role='combobox']").send_keys(person)


    @allure.step("Клик на кнопку поиска в модуле поиска.")
    def click_search_button(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    @allure.step("Подождать пока откроется окно с рекламой и закрыть его.")
    def advertising(self) -> None:
        WebDriverWait(self.url, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.styles_root__W1oqS")))
        self.url.find_element(By.CSS_SELECTOR, "button.styles_root__EjoL7").click()


    @allure.step("Кликнуть по первому элементу списка фильмов.")
    def first_on_the_list(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "a[href='/film/1108577/sr/1/']").click()


    @allure.step("Кликнуть по кнопке фильтра.")
    def filtering(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "a[href='/s/']").click()
 

    @allure.step("Выбрать фильтрацию по стране.")
    def filter_by_country(self, country: str) -> None:
        self.url.find_element(By.XPATH, f"//option[contains(value, '') and text()='{country}']").click()


    @allure.step("Выбрать фильтрацию по году.")
    def filter_year(self, year: int) -> None:
        self.url.find_element(By.CSS_SELECTOR, "input[id='year']").send_keys(year)


    @allure.step("Выбрать фильтрацию по жанру.")
    def filter_by_genre(self, genre: str) -> None:
        self.url.find_element(By.XPATH, f"//option[contains(value, '') and text()='{genre}']").click()


    @allure.step("Нажать кнопку 'поиск' в разделе 'фильтры'.")
    def filter_search(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "input[value='поиск']").click()


    @allure.step("Открыть фильм после фильтрации.")
    def open_movie(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "a[href='/film/41543/sr/1/']").click()


    @allure.step("Проверка результата фильтрации по стране.")
    def filter_result_country(self) -> None:
        return self.url.find_element(By.CSS_SELECTOR, 'a[href="/lists/movies/country--2/?b=films&b=top"]').text
    

    @allure.step("Проверка результата фильтрации по году.")
    def filter_result_year(self) -> None:
        return self.url.find_element(By.CSS_SELECTOR, 'a[href="/lists/movies/year--1993/?b=films&b=top"]').text


    @allure.step("Проверка результата фильтрации по жанру.")
    def filter_result_genre(self) -> None:
        return self.url.find_element(By.CSS_SELECTOR, 'a[href="/lists/movies/genre--comedy/?b=films&b=top"]').text
       

    @allure.step("Получение 'случайного фильма'.")
    def random_movie(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "input#search").click()
        WebDriverWait(self.url, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.right")))

    @allure.step("Авторизация до момента введения кода с картинки.")
    def authorization(self, login: str, password: str) -> None:
        self.url.find_element(By.CSS_SELECTOR, "button.styles_loginButton__LWZQp").click()
        self.url.find_element(By.CSS_SELECTOR, "input#passp-field-login").send_keys(login)
        self.url.find_element(By.CSS_SELECTOR, "button[aria-disabled='false']").click()
        self.url.find_element(By.CSS_SELECTOR, "input#passp-field-passwd").send_keys(password)
        self.url.find_element(By.CSS_SELECTOR, "button[aria-disabled='false']").click()


    @allure.step("Получение списка фильмов 'Топ 250'")
    def top_250(self) -> None:
        self.url.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/nav/ul/li[3]/a").click()
        self.url.find_element(By.CSS_SELECTOR, "div.styles_meta__M_kDW").click()
        return self.url.find_element(By.CSS_SELECTOR, 'h1.styles_title__jB8AZ').text


    @allure.step("Нажатие кнопки 'восстановить доступ' и возвращение текста с страницы.")
    def risk_hacking(self) -> None:
        self.url.find_element(By.CSS_SELECTOR, "div.Info-action").click()
        return self.url.find_element(By.CSS_SELECTOR, "h1.passp-title").text
