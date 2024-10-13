# final_work_kinopoisk
## Автоматизированные UI- и API-тесты из финальной работы по ручному тестированию "Кинопоиск"
### Задача проекта: провести проверку модуля поиска (фильм/сериал/персона), филтрации фильмов и возможности авторизации на сайте Кинопоиск. Проект состоит из 6 ui тестов и 6 api тестов

## Ссылка на финальную работу по ручному тестированию:
[(https://steady-guava-8a6.notion.site/a715e310077c4e1eb9c584b9348ee2b8)]

## Проект содержит файлы:
- **config.py** - файл с данными, которые используются для авторизации на сайте (логин и пароль), url адреса для ui и api тестов, содержит также информацию о заголовке и токене, передаваемых в api тестах.

- **page_api.py** - содержит методы класса API поиска фильма/сериала, наград а так же персоны с использованием Api. Методы поиска фильма/сериала по названию, id, дополнительным полям, по наградам, поиск персон по фамилии и имени, по ID.

- **page_ui.py** - файл с методами класса UI. В данном файле находятся методы: обработка рекламы, ввдедение данных в поисковую строку, нажатие кнопки "найти", нажатие кнопки "фильтр", получения информация на странице результата поиска, методы поиск персоны и случайного фильма (пустого поиска), а также авторизация на сайте. 

- **pytest.ini** - файл с указанием, какого формата файлы должны запускаться в pytest.

- **test_api.py** -  файл с тестами api. Тесты запускаются командой  pytest -k test_api.py.

- **test_ui.py** - файл с тестами api. Тесты запускаются командой  pytest -k test_ui.py.

- **requirements.txt** -  файл с используемыми зависимостями в проекте. Установить зависимости на тестовый стенд можно командой pip install -r requirements.txt

## Как запустить тесты для формирования отчета
1. Открыть терминал и перейти к рабочей директории: cd final_work_kinopoisk>
2. Запустить тесты и указать  путь к каталогу результатов тестирования: **pytest --alluredir allure-result**.
3. В директории с тестами появится папка **allure-result**. Там сохранятся отчеты о тестах.
4. Запустить и конвертировать результаты теста в отчет с помощью команды **allure serve allure-result**. 

## Как просмотреть сформированный отчет
1. После ввведения команды **allure serve allure-result** сгенерируется отчет о тестах.
2. Отчет откроется на локальном сервере в окне вашего браузера.
3. **Overview** — раздел с общей информацией: сколько всего тестов запустили, процент успешных тестов, доля успешных и неуспешных тестов.
В разделе **Suits** — список тестов и конкретная информация о каждом из них.