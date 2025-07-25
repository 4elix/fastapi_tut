from pydantic import BaseModel
from typing import List


class NewsBase(BaseModel):
    title: str
    content: str


class NewsCreate(NewsBase):
    category_id: int


class NewsOut(NewsBase):
    id: int
    category_id: int

    class Config:
        orm_model = True
        # Модель ответа клиенту. orm_mode = True — позволяет преобразовывать ORM-объекты в JSON.


class CategoryBase(BaseModel):
    name: str


class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_model = True
