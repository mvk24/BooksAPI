from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()


# DEFINING THE DATA MODEL WITH VALIDATION
class Book(BaseModel):
    id: int
    title: str = Field(..., min_length = 3, max_length = 100, description = "Title must be between 3-100 characters long.")
    author: str = Field(..., min_length = 3, description = "Author name should be atleast 3 characters.")
    YOP: Optional[int] = None
    description: str = Field(..., min_length = 5, max_length = 100, description = "Please provide a decsription of length 5-100 characters.")
    price: float = Field(..., gt = 0)


# LOCAL IN MEMORY LIST TO STORE DEFAULT BOOK RECORDS, USER INPUT VIA SWAGGER UI ARE ACCEPTED.
books: List[Book] = [
    Book(id = 0, title = "Python", author = "Varun", YOP = 2025, description = "Good Python Book.", price = 777),
    Book(id = 1, title = "DSA", author = "MVK", description = "Good DSA Book.", price = 500.99),
    Book(id = 2, title = "Java", author = "MVK", description = "Java best seller.", price = 600)
]


# TO ADD NEW BOOK
@app.post("/books", response_model = Book, response_model_exclude_none = True)
def create_book(book:Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail=f"Book with ID {book.id} already exists.")

    books.append(book)
    return book



# GET ALL BOOKS WITHOUT FILTERS
@app.get("/books")
def get_all_books():
    return books



# FILTER BOOKS BY AUTHOR & TITLE (QUERY PARAMATER)
@app.get("/books/filter")
def filter_books(author: Optional[str] = None, title: Optional[str] = None):
    if author is None and title is None:
        return{"All Books": books}
    filtered_books = books
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book.author.lower()]
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book.title.lower()]
    return filtered_books



# GET BOOKS BY ID ( PATH PARAMETER )
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found.")



# DELETE BOOKS BY ID ( PATH PARAMETER )
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
        for index, book in enumerate(books):
            if book.id == book_id:
                del_book = books.pop(book_id)
                return{"Success": "Book deleted successfully.", "book": del_book}
        raise HTTPException(status_code=404, detail="Book not found.")
    


# UPDATE BOOKS BY ID ( PATH PARAMETER + REQUEST BODY )
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            if updated_book.id != book_id and any(b.id == updated_book.id for b in books):
                raise HTTPException(status_code=400, detail="Updated ID already exists for another book. Please change the ID.")
            books[index] = updated_book
            return{"message": "Book Updated", "book": updated_book}
        
    raise HTTPException(status_code = 404, detail = "Book not found")




