from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return 'Hi new app 2!'
