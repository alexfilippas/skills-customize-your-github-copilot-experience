from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books = [
    {"id": 1, "title": "Intro to Python", "author": "J. Lee"},
    {"id": 2, "title": "APIs for Beginners", "author": "R. Patel"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Books API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(book: Book):
    for existing_book in books:
        if existing_book["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    new_book = book.model_dump()
    books.append(new_book)
    return new_book
