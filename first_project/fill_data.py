from sqlalchemy.orm import Session
from database import SessionLocal
import models

db: Session = SessionLocal()

# Добавление категорий
categories = ["Политика", "Экономика", "Технологии", "Спорт", "Культура"]

for name in categories:
    category = models.Category(name=name)
    db.add(category)

db.commit()

# Добавление новостей
news_data = [
    ("Выборы в парламент", "Сегодня состоялись выборы в парламент страны.", 1),
    ("Курс доллара вырос", "Курс доллара по отношению к евро вырос на 2%.", 2),
    ("Новый iPhone представлен", "Apple представила новую модель iPhone с ИИ.", 3),
    ("Чемпионат мира по футболу", "Сборная Франции выиграла у Германии 2:1.", 4),
    ("Открытие театрального сезона", "Большой театр открыл новый сезон спектаклем.", 5),
]

for title, content, category_id in news_data:
    news = models.News(title=title, content=content, category_id=category_id)
    db.add(news)

db.commit()
db.close()

