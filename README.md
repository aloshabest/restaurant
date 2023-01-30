### Описание
REST API для ресторана.
### Технологии
* [![Python](https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
* [![SQLalchemy](https://img.shields.io/badge/SQLAlchemy-198754.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAMAAAApB0NrAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAACKFBMVEX////+/v76+vr19fX39/fq6uru7u79/f37+/vGxsaFhYV0dHSenp7BwcG8vLzz8/Ozs7NycnJWVlZeXl6Wlpbt7e2cnJyBgYGCgoKNjY3e3t7xuLbqko7++Pjv7++Xl5dnZ2d/f39NTU1XV1fX19fg4OB4eHiOjo5bW1s/Pz+IiIjR0dFYWFhGRkaysrL88vLfVk/WKiD0x8bh4eG1tbWioqL8/Pxvb2/Z2dldXV1QUFBsbGxUVFTn5+fxt7XbQjrWJhvkcm3++/ttbW329vaampqYmJi6urpCQkKRkZFLS0v5+fnm5ub99vbjb2ruq6ngYFnXLyX1zMujo6OgoKCVlZVwcHBDQ0O9vb2wsLCUlJRVVVX4+Phubm7zwb/fWVP31tbrmpfVIRbld3HHx8dlZWVhYWHW1tanp6dOTk5RUVHDw8NxcXF9fX3l5eXs7e3//PzldnLgY13mhoPmgX3bQzrYMij1zs2Li4vi4uLx8fHFxcXJycmdnZ1ERESfn5/Q0NBaWlrOzs709PTZ3Nz3zs3iZ2L76+v//v7WKB3leHP+/PzT09NHR0esrKzExMSMjIxlZmbm09PiZF/fWlX319b9+Pjvr63YNCrXMCbrmJbf39+tra2mpqaSkpK5ubm/v7++vr7Fxsb03t3vqabvq6j1z8798/PwsrDuqKXup6Tvrqxra2tjY2Pw8PDKysp7e3vy8vKvr6/IyMhZWVmDg4Pa2trp6ek/ESbeAAAAAWJLR0QAiAUdSAAAAAd0SU1FB+cBGwoqD4+uLNsAAAFgSURBVBgZ7cFNKEMBAAfw///t7cvHtkeSpsWWZCkfoTlILZTPq7Z2FAe1oriQA1HKTVxcFYdRMknkwMVF0WTNwbCinDQHtvbMe8pnOXPY74eMf4UCoIFC1OoI6Ek98QVh4Js4zHyT1FNxC5WVjAGijeSDRMbLUtqEgWSkmOQ5VFUkY4CoSecfaxxkQV4oIcNFFoYbyRRUZpLufQg5Dkl0RyVTreSUgSOLJavdADNU3RYVoJEFa4XRbszOilSGANTk5Eomc+ICCpdRJUXZR8ZXB2K2tEAuwGfhUsrzcnMIP9/NUhg9rSavSqfHuddKWeSE7+7p6nbqoJnkbtu8n+TcRfk0i+7jz77ax0BTpGuoIdzj2PGseKkYXKSqpfekhpfXywBc/btrSXSW1JHb6KDCu0IFPon1gTXnZCew7sc3Aj6MnA0LMxH72IZowm8IwLdZGgxs6fAN8YMQlMV2ZPyBV6bMXOnSHdMrAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIzLTAxLTI3VDEwOjQxOjU1KzAwOjAwEw/7UQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMy0wMS0yN1QxMDo0MTo1NSswMDowMGJSQ+0AAAAASUVORK5CYII=)](https://www.sqlalchemy.org/)
* [![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
* [![Docker](https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
### Запуск проекта
- В корневой папке создать файл .env и внести свои данные базы данных PostgreSQL:
```
DB_NAME=<название вашей базы данных>
POSTGRES_USER=<ваше имя пользователя>
POSTGRES_PASSWORD=<ваш пароль>
DB_HOST=<ваш хост>
DB_PORT=<ваш порт>
SQLALCHEMY_DATABASE_URL="postgresql://<ваше имя пользователя>:<ваш пароль>@<ваш хост из docker-compose>/<название вашей базы данных>"

REDIS_HOST=<ваш хост redis>
REDIS_PORT=<ваш порт redis>
REDIS_DB=0
```
- Выполнить команду:
```
docker-compose up --build
```
- Запустить сайт:
```
http://127.0.0.1:8000/api/v1/
```
- Запуск тестов:
```
docker-compose -f docker-compose.tests.yml up --build
```

Другой вариант:
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
