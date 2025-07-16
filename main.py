from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
books = []

class Book(BaseModel):
    id: int
    title: str
    author: str

@app.post("/books")
def create_book(book:Book):
    books.append(book)
    return{"Successfull": "Book added successfully", "book": book.dict()}

@app.get("/books")
def get_all_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return("Error: Book does not exists.")
    else:
        return books[book_id]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return("Error: Book does not exists")
    else:
        del_book = books.pop(book_id)
        return{"Success": "Book deleted successfully.", "book": del_book.dict()}