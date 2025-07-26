from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str

books: List[Book] = []


# TO ADD NEW BOOK

@app.post("/books")
def create_book(book:Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail=f"Book with ID {book.id} already exists.")

    books.append(book)
    return{"Successfull": "Book added successfully", "book": book.dict()}



# GET ALL BOOKS WITHOUT FILTERS

@app.get("/books")
def get_all_books():
    return books


# GET BOOKS BY ID

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return("Error: Book does not exists.")
    else:
        return books[book_id]



# DELETE BOOKS BY ID

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return("Error: Book does not exists")
    else:
        del_book = books.pop(book_id)
        return{"Success": "Book deleted successfully.", "book": del_book.dict()}


# UPDATE BOOKS BY ID

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if books.id == book_id:
            if update_book.id != book_id and any(b.id == update_book.id for b in books):
                raise HTTPException(status_code=400, detail="Updated ID already exists for another book. Please change the ID.")
            books[index] = update_book
            return{"message": "Book Updated", "book": update_book}
        
    raise HTTPException(status_code = 404, detail = "Book not found")




# FILTER BOOKS BY AUTHOR (QUERY PARAMATER)
