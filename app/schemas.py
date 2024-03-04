from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint


class User(BaseModel):
    email: EmailStr


class UserCreate(User):
    password: str


class UserOut(User):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
