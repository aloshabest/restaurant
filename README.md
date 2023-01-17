### Описание
REST API для ресторана.
### Технологии
Python 3.9

FastAPI 0.89.1

SQLAlchemy 1.4.46
### Запуск проекта 
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/scripts/activate
``` 
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке core создать файл .env и внести свои данные базы данных PostgreSQL:
```
SQLALCHEMY_DATABASE_URL="postgresql://<ваше имя пользователя>:<ваш пароль>@localhost/<название вашей базы данных>"
``` 
- Выполните миграции
```
alembic revision --autogenerate -m "create tables"
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