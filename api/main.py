from typing import AsyncGenerator, List
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager

from routers.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    yield


app = FastAPI()
routers: List[APIRouter] = [users_router]
[app.include_router(router) for router in routers]
