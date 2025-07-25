from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    age: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    body: str
    author_id: int


class PostResponse(PostBase):
    id: int
    author: User

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class UserCreate(UserBase):
    pass


