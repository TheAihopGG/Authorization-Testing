from fastapi import APIRouter
from .dependencies import *

router = APIRouter(prefix=...)
__all__ = ("router",)
