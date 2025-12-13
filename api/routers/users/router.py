from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from psycopg import AsyncConnection

from core.dependencies import get_async_connection
from services.users import get_user_by_id
from .schemas import GetUser

router = APIRouter(prefix="/api/users")


@router.get("/get-user")
async def get_user_endpoint(
    data: GetUser,
    aconn: AsyncConnection = Depends(get_async_connection),
) -> JSONResponse:
    if user := await get_user_by_id(aconn, data.user_id):
        return JSONResponse(
            {
                "id": user,
                "name": user.name,
                "email_confirmed": user.email_confirmed,
            }
        )
    else:
        return JSONResponse({"detail": "Unknown user"}, status_code=404)


__all__ = ("router",)
