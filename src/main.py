from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from operations.router import router as router_operation
from pages.router import router as pages_router

from redis import asyncio as aioredis

from tasks.routes import tasks_router

app = FastAPI(
    title="Trading App"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_operation)

app.include_router(tasks_router)

app.include_router(pages_router)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.on_event("startup")  # execute when fastapi app startup
async def startup():
    # https://redis.io/docs/connect/clients/python/
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
