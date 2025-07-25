# pip install fastapi uvicorn sqlalchemy

from fastapi import FastAPI

import models
from routers import news
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(news.router)
