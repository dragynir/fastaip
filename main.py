from fastapi import FastAPI

app = FastAPI(title="Backend")


fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Alice'},
    {'id': 2, 'role': 'traider', 'name': 'Bob'},
]


# Пример передачи параметра в пути запроса
@app.get("/users/{user_id}")
def get_user(user_id: int):  # тайпхинт важен, т к по нему user_id из строки кастуется к int
    """Get user from database."""
    return [user for user in fake_users if user['id'] == user_id]
