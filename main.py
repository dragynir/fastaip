from fastapi import FastAPI

app = FastAPI(title="Backend")


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Alice'},
    {'id': 2, 'role': 'traider', 'name': 'Bob'},
]


# Пример передачи параметра пути user_id в пути запроса
# Возвращаем список, который автоматисески сериализуется (конвертация в json)
# Пример запроса
# curl -X 'GET' \
#   'http://127.0.0.1:8000/users/1' \
#   -H 'accept: application/json'
@app.get("/users/{user_id}")
def get_user(user_id: int):  # тайпхинт важен, т к по нему user_id из строки кастуется к int
    """Get user from database."""
    return [user for user in fake_users if user['id'] == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'btc'},
    {'id': 2, 'user_id': 2, 'currency': 'btc'},
]

# Пример передачи параметров
# Также тут проставлены дефолтные параметры
# Пример запроса
# curl -X 'GET' \
#   'http://127.0.0.1:8000/trades/?limit=1&offset=1' \
#   -H 'accept: application/json'
@app.get("/trades/")
def get_trades(limit: int = 0, offset: int = 1):
    return fake_trades[offset:][:limit]


fake_users2 = [
    {'id': 1, 'role': 'admin', 'name': 'Alice'},
    {'id': 2, 'role': 'traider', 'name': 'Bob'},
]


# Пример обновления данных в базу
# Эндпоинт оставили тот же "/users/{user_id}"
# curl -X 'POST' \
#   'http://127.0.0.1:8000/users/1?new_name=cat' \
#   -H 'accept: application/json' \
#   -d ''
@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user['id'] == user_id, fake_users2))[0]
    current_user['name'] = new_name
    return {'status': 200, "data": current_user}

