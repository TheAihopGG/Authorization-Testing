from typing import AsyncGenerator, Iterable
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


app = FastAPI()
routers: Iterable[APIRouter]
[app.include_router(router) for router in routers]
