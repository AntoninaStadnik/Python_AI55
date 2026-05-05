# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –-host localhost --reload
# Напишіть клієнта який робить запит на сервер

import json

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#
# class Response(BaseModel):
#     message: str
#
#
# @app.post("/hello")
# def hello_world() -> Response:
#     return Response(
#         message="Hello World",
#     )

# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва
# сервери

# class HelloResponse(BaseModel):
#     message: str
#
#
# @pp.get("/greeting")
# def greeting() -> HelloResponse:
#     return HelloResponse(
#         message="Hello from server1"
#     )

# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


@app.get("/books")
def get_books() -> list[Book]:
    with open("books.json", "rb") as f:
        books_data = json.load(f)
        return [Book(**book) for book in books_data]
