

Launch

uvicorn main:app --reload


http://127.0.0.1:8000 - тут будет приложение

http://127.0.0.1:8000/docs - тут будет дока swagger api


Инициализация миграций:

`alembic init migrations`


Инициализация миграций:

alembic revision --autogenerate -m "database creation"


# main:app название файла: название переменной с экземпляром FastAPI
# --reload автоматически перезагружает если изменился код