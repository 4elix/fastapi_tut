from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create_engine -> для подключения к БД.
# sessionmaker -> создание сессий (соединений).
# declarative_base -> базовый класс для ORM-моделей.

SQLALCHEMY_DB_URL = 'sqlite:///./news.db'

engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={'check_same_thread': False}
)
# check_same_thread=False -> требуется для работы SQLite с FastAPI.

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# SessionLocal -> класс, который создаёт сессии для взаимодействия с БД.

Base = declarative_base()
# Base -> базовый класс для моделей (Category, News).
