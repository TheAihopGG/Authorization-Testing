from typing import AsyncGenerator
from psycopg import AsyncConnection

from core.config import POSTGRES_CONNINFO


async def get_async_connection() -> AsyncGenerator[AsyncConnection]:
    aconn = await AsyncConnection.connect(POSTGRES_CONNINFO)
    try:
        await aconn.execute("BEGIN;")
        yield aconn
    except Exception as err:
        await aconn.execute("ROLLBACK;")
        raise err
    else:
        await aconn.execute("COMMIT;")
    finally:
        await aconn.close()


__all__ = ("get_async_connection",)
