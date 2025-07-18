from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
books = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str

books: List[Book] = []

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


@app.put("/books/{book_id}")
def update_book(book_id: int, new_book: Book):
    for i in range(len(books)):
        if books[i].id == book_id:
            books[i] = new_book
            return{"Book updated successfully" : new_book}
        
    raise HTTPException(status_code = 400, detail = "Book not found")
