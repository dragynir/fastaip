

Launch

`uvicorn main:app --reload`


http://127.0.0.1:8000 - тут будет приложение

http://127.0.0.1:8000/docs - тут будет дока swagger api


Launch celery workers

`celery -A tasks.tasks:celery worker --loglevel=INFO --pool=solo`

# Каждый раз надо перезапускать celery т к он не может в autoreload
# tasks.tasks:celery - переменная с экземпляром Celery
# --pool=solo - only for windows (cause of bugs)


Launch flower for workers monitoring

`celery -A tasks.tasks:celery flower`

http://localhost:5555/ - тут будет интерфейс flower


Инициализация миграций:

`alembic init migrations`


Генерация миграций: (создается python файл в versions с методами upgrade и downgrade)

`alembic revision --autogenerate -m "database creation"
`
Применение миграции (upgrade), где 2d96667cd6a1 - это revision из .py файла миграции

`alembic upgrade 2d96667cd6a1
`


Применим до самой последней миграции
`alembic upgrade head
`


# main:app название файла: название переменной с экземпляром FastAPI
# --reload автоматически перезагружает если изменился код


TODO

нужно будет все в Docker обернуть


# Deploy


docker build . -t fastapi_app:latest
docker run -p 7329:8000 fastapi_app

# SMTP_service