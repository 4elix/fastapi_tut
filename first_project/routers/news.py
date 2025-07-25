from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal

import models, schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/categories', response_model=List[schemas.CategoryOut])
def get_categories(db: SessionLocal = Depends(get_db)):
    return db.query(models.Category).all()


@router.get('/news', response_model=List[schemas.NewsOut])
def get_news(db: SessionLocal = Depends(get_db)):
    return db.query(models.News).all()


@router.get('/news/category/{category}', response_model=List[schemas.NewsOut])
def get_news_by_category(category_id: int, db: SessionLocal = Depends(get_db)):
    return db.query(models.News).filter(models.News.category_id == category_id).all()
