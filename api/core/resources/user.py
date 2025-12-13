from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    password_hash: bytes
    email: str
    email_confirmed: bool


__all__ = ("User",)
