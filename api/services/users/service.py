from psycopg import AsyncConnection

from core.resources import User


async def get_user_by_id(aconn: AsyncConnection, id: int) -> User | None:
    async with aconn.cursor() as acur:
        await acur.execute("SELECT * FROM users WHERE id = %s", (id,))
        result = await acur.fetchone()
    return User._make(result) if result else None


__all__ = ("get_user_by_id",)
