### Описание
REST API для ресторана.
### Технологии
* [![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
* [![SQLalchemy](https://img.shields.io/badge/SQLAlchemy-198754.svg?style=for-the-badge&logo=data:image/png;base64,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)](https://www.sqlalchemy.org/)
* [![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
* [![Docker](https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
### Запуск проекта 
- В корневой папке создать файл .env и внести свои данные базы данных PostgreSQL:
```
DB_NAME=<название вашей базы данных>
POSTGRES_USER=<ваше имя пользователя>
POSTGRES_PASSWORD=<ваш пароль>
DB_HOST=<ваш хост из docker-compose>
DB_PORT=<ваш порт>
SQLALCHEMY_DATABASE_URL="postgresql://<ваше имя пользователя>:<ваш пароль>@<ваш хост из docker-compose>/<название вашей базы данных>"
```
- Выполнить команду:
```
docker-compose up --build
```
- Запустить сайт:
```
http://127.0.0.1:8000/api/v1/
```
### Запуск тестов:
В корневой создать файл .env.test и внести свои данные тестовой базы данных PostgreSQL:
```
DB_NAME=<название вашей тестовой базы данных>
POSTGRES_USER=<ваше имя тестового пользователя>
POSTGRES_PASSWORD=<ваш тестовый пароль>
DB_HOST=<ваш тестовый хост из docker-compose>
DB_PORT=<ваш тестовый порт>
SQLALCHEMY_DATABASE_URL="postgresql://<ваше имя тестового пользователя>:<ваш тестовый пароль>@<ваш тестовый хост из docker-compose>/<название вашей тестовой базы данных>"
```
- Выполнить команду:
```
docker-compose -f docker-compose.tests.yml up --build
```

### Другой вариант запуска проекта:
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/scripts/activate
``` 
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В корневой папке создать файл .env и внести свои данные базы данных PostgreSQL:
```
SQLALCHEMY_DATABASE_URL="postgresql://<ваше имя пользователя>:<ваш пароль>@localhost/<название вашей базы данных>"
```
- Выполните миграции
```
alembic upgrade head
``` 
- Выполните команду:
```
uvicorn main:app --reload
```
- Запустите сайт:
```
http://127.0.0.1:8000/api/v1/
```

### Методы сервиса
МЕНЮ:
- /menus/
```
Принимает запрос: GET: выдаёт список всех меню, количество их подменю и блюд;
Принимает запрос: POST: создаёт меню, количество их подменю и блюд.
```
- /menus/{menu_id}
```
Принимает запрос: GET: выдаёт информацию о конкретном меню, количество подменю и блюд;
Принимает запрос: PATCH: обновляет конкретное меню, количество подменю и блюд;
Принимает запрос: DELETE: удаляет конкретное меню.
```
ПОДМЕНЮ:
- /menus/{menu_id}/submenus
```
Принимает запрос: GET: выдаёт список всех подменю и количетсво блюд;
Принимает запрос: POST: создаёт подменю и количетсво блюд.
```
- /menus/{menu_id}/submenus/{submenu_id}
```
Принимает запрос: GET: выдаёт информацию о конкретном подменю и количетсво блюд;
Принимает запрос: PATCH: обновляет конкретное подменю и количетсво блюд;
Принимает запрос: DELETE: удаляет конкретное подменю.
```
БЛЮДА:
- /menus/{menu_id}/submenus/{submenu_id}/dishes
```
Принимает запрос: GET: выдаёт список всех блюд;
Принимает запрос: POST: создаёт блюдо.
```
- /menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}
```
Принимает запрос: GET: выдаёт информацию о конкретном блюде;
Принимает запрос: PATCH: обновляет конкретное блюдо;
Принимает запрос: DELETE: удаляет конкретное блюдо.
