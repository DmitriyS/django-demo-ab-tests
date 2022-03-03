# Описание

Демо-приложение: Django + DRF + функциональные тесты + Docker

# Задача

Необходимо разработать систему позволяющую команде аналитиков совместно с разработчиками мобильного приложения проводить А/Б тестирование.

Пример использования:
- Аналитики придумывают некоторые количество тестов, например:
  25 процентам пользователей показать зеленый фон, 25 процентам красный фон, а оставшимся 50 - филетовый. 
- Аналитики заводят в админку АБ тесты и их группы. В каждой указывают вероятность выпадения того или иного значения, например:
  тест с тремя тестовыми группами: green / red / violet с вероятностями 25 / 25 / 50 соответсвенно 
- Мобильное приложение осуществляет запрос к серверу указывая рекламный идентификатор (IDFA) в запросе и получает массив всех значений для каждого А/Б теста. Например:
```json
[
    {
        "name": "background_01",
        "value": "green"
    },
    {
        "name": "subscription_01",
        "value": "montly"
    }
]
```
- Важно чтобы каждый раз при запросе с одним и тем же IDFA пользователь получал один и тот же результат по каждому из тестов при этом попадая в разные тестовые группы по каждому из них (То есть человек с одним IDFA не должен всегда попадать в первую группу первого теста, в первую группу второго теста и т.д. т.п.).
- Ориентируясь на оговоренные заранее варианты значений для каждого теста, мобильное приложение ведет себя по разному для разных пользователей.
- Аналитики проводят исследование на основе данных от мобильного приложения

Необходимо разработать на базе Django:
1. Админку для заведения А/Б тестов и их групп
2. REST API для получения мобильным приложением списка А/Б тестов и выпавшем значении по каждому из тестов
3. REST API для получения списка заведенных А/Б тестов с их группами и вероятностями каждой

# Установка

- python 3.10+
- pip install -r requirements_dev.txt
- python manage.py migrate

# Запуск

- python manage.py runserver 8000

# Конфигурация

- python manage.py createsuperuser
- localhost:8000/admin/

# Использование

- http -v localhost:8000/experiments/
- http -v localhost:8000/groups/ idfa==123

# Тесты

- python manage.py test [-k test_name]
