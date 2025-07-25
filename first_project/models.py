from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    news = relationship('News', back_populates='category')


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='news')



