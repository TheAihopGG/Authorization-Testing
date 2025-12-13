from typing import NamedTuple


class User(NamedTuple):
    id: int
    name: str
    password_hash: bytes
    email: str
    email_confirmed: bool


__all__ = ("User",)
