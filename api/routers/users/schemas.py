from pydantic import BaseModel, Field


class GetUser(BaseModel):
    user_id: int = Field(gt=0)


__all__ = ("GetUser",)
