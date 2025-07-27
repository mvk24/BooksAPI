from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum


app = FastAPI()


# ENUM FOR VALID GENERS
class GenereNum(str, Enum):
    fi = "fiction"
    sc = "science"
    his = "history"
    te = "tech"



# DEFINING THE DATA MODEL WITH VALIDATION
class Book(BaseModel):
    id: int
    title: str = Field(..., min_length = 3, max_length = 100, description = "Title must be between 3-100 characters long.")
    author: str = Field(..., min_length = 3, description = "Author name should be atleast 3 characters.")
    genere: str
    YOP: Optional[int] = None
    description: str = Field(..., min_length = 5, max_length = 100, description = "Please provide a decsription of length 5-100 characters.")
    price: float = Field(..., gt = 0)


# LOCAL IN MEMORY LIST TO STORE DEFAULT BOOK RECORDS, USER INPUT VIA SWAGGER UI ARE ACCEPTED.
books: List[Book] = [
    Book(id = 0, title = "Python", author = "Varun", genere = "tech", YOP = 2025, description = "Good Python Book.", price = 777),
    Book(id = 1, title = "DSA", author = "MVK", genere = "science", description = "Good DSA Book.", price = 500.99),
    Book(id = 2, title = "Java", author = "MVK", genere = "fiction", description = "Java best seller.", price = 600)
]


# TO ADD NEW BOOK
@app.post("/books", response_model = Book, tags = ["Books"], summary = "Add a new book.", description = "Insert a new book into the In memory list.", response_description = "The book added to the system.", response_model_exclude_none = True, status_code = 201)
def create_book(book:Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code = 400, detail = f"Book with ID {book.id} already exists.")
    books.append(book)
    return book



# GET ALL BOOKS WITHOUT FILTERS
@app.get("/books", tags = ["Books"], summary=  "Get all books.", description = "Retrieve a list of all available books in the memory.", response_description="List of Books in memory", response_model = List[Book], status_code = 200)
def get_all_books():
    return books


# GET THE FIRST BOOK
@app.get("/books/first", tags = ["Books"], summary = "First Book in memory list", description = "Return the first available book from the memory system", response_description = "The first book object",response_model = Book)
def first_book():
    if not books:
        raise HTTPException(status_code = 404, detail = "Book not found.")
    return books[0]
    


# GET BOOKS BY GENERE
@app.get("/books/genere/{genere}", response_model = List[Book], tags = ["Books"], summary = "Get Books by Genere", description = "Retrieve all books that match a specific genere using Enum", response_description = "List of Books filtered by Genere")
def get_book_by_genere(genere: GenereNum):
    filtered_books = [book for book in books if book.genere == genere.value]
    if not filtered_books:
        raise HTTPException(status_code = 404, detail = "No books found in this genere.")
    return filtered_books




# FILTER BOOKS BY AUTHOR & TITLE (QUERY PARAMATER)
@app.get("/books/filter", response_model = List[Book], tags = ["Books"], summary = "List of Filtered books.", description = "Filter books by author AND/OR title using Path and Query Parameters.", response_description = "List of filtered books")
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
@app.get("/books/{book_id}", response_model = Book, tags = ["Books"], summary = "Get Book by ID", description = "Fetch a single book usings its ID", response_description = "Matching Book", status_code = 200)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code = 404, detail = "Book not found.")



# DELETE BOOKS BY ID ( PATH PARAMETER )
@app.delete("/books/{book_id}", response_model = Book, status_code = 200, tags = ["Books"], summary = "Delete Book by ID", description = "Delete a book from the memory List using its ID", response_description = "Deleted book")
def delete_book(book_id: int):
        for index, book in enumerate(books):
            if book.id == book_id:
                del_book = books.pop(index)
                return{"Success": "Book deleted successfully.", "book": del_book}
        raise HTTPException(status_code = 404, detail="Book not found.")
    


# UPDATE BOOKS BY ID ( PATH PARAMETER + REQUEST BODY )
@app.put("/books/{book_id}", response_model = Book, status_code = 200, tags = ["Books"], summary = "Update Book by ID", description = "Update the details of a specific book using its ID", response_description = "Updatated Book Object")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            if updated_book.id != book_id and any(b.id == updated_book.id for b in books):
                raise HTTPException(status_code = 400, detail = "Updated ID already exists for another book. Please change the ID.")
            books[index] = updated_book
            return{"message": "Book Updated", "book": updated_book}
        
    raise HTTPException(status_code = 404, detail = "Book not found")




