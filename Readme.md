

Launch

uvicorn main:app --reload


http://127.0.0.1:8000 - тут будет приложение

http://127.0.0.1:8000/docs - тут будет дока swagger api


Инициализация миграций:

`alembic init migrations`


Генерация миграций: (создается python файл в versions с методами upgrade и downgrade)

`alembic revision --autogenerate -m "database creation"
`
Применение миграции (upgrade), где 2d96667cd6a1 - это revision из .py файла миграции

`alembic upgrade 2d96667cd6a1
`



# main:app название файла: название переменной с экземпляром FastAPI
# --reload автоматически перезагружает если изменился код