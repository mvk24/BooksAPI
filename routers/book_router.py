from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from models.book_model import Book
from schemas.book_schema import BookCreate, BookOut, BookUpdate
from db import get_db
from utils.token import get_cuurent_user
from dependencies.roles import admin_only


# DEPENDENCIES is used to enforese authentication mandatory for all routes
router = APIRouter(prefix = "/books", tags = ["Books DB"], dependencies = [Depends(get_cuurent_user)])


# Create new book
@router.post("/", response_model = BookOut, status_code = 201, summary = "Add a new book(ADMIN ONLY)",description = "Insert a new book into the DB.", response_description = "The book added to the system.", response_model_exclude_none = True)
def create_book(book: BookCreate, db : Session = Depends(get_db), current_user: dict = Depends(admin_only)):
    existing = db.query(Book).filter(Book.title == book.title).first()
    if existing:
        raise HTTPException(status_code = 400, detail = "Book with this title already exists.")
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

    


# Get all books
@router.get("/", response_model = List[BookOut],  summary=  "Get all books", description = "Retrieve a list of all available books in the memory.", response_description="List of Books in memory", status_code = 200)
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books
    



# Get Book by ID
@router.get("/{book_id}", response_model = BookOut, summary = "Get Book by ID", description = "Fetch a single book usings its ID", response_description = "Matching Book", status_code = 200)
def read_books_id(book_id: int, db:Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    return book


# Get books by Genre
@router.get("/genre/{genre}", response_model = List[BookOut], summary = "Get Books by Genre", description = "Retrieve all books that match a specific genre", response_description = "List of Books filtered by Genre")
def get__book_by_genre(genre: str, db:Session = Depends(get_db)):
    books = db.query(Book).filter(Book.genre.ilike(f"%{genre}%")).all()
    if not books:
        raise HTTPException(status_code = 404, detail = "No books are found with this genre")
    return books


# Filter Books by Author AND/OR Title
@router.get("/search/", response_model = List[BookOut], summary = "Search books by author/title", description = "Filter books by author AND/OR title using Path and Query Parameters.", response_description = "List of filtered books")
def search_books(title: Optional[str] = None,
                 author: Optional[str] = None,
                 db:Session = Depends(get_db)):
        query = db.query(Book)
        if title:
            query = query.filter(Book.title.ilike(f"%{title}%"))
        if author:
            query = query.filter(Book.author.ilike(f"%{author}%"))
        books = query.all()
        if not books:
            raise HTTPException(status_code = 404, detail = "No matching books found")
        return books

        


# Update book by ID
@router.put("/{book_id}", response_model = BookOut, summary = "Update Book by ID(ADMIN ONLY)", description = "Update the details of a specific book using its ID", response_description = "Updatated Book Object", status_code = 200)
def update_book(book_id: int, updated_book: BookUpdate, db:Session = Depends(get_db), current_user: str = Depends(admin_only)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    for key, value in updated_book.model_dump(exclude_unset = True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


# Delete book by ID
@router.delete("/{book_id}", response_model = BookOut, summary = "Delete Book by ID(ADMIN ONLY)", description = "Delete a book from the memory List using its ID", response_description = "Deleted book", status_code = 200)
def delete_book(book_id: int, db:Session = Depends(get_db), current_user: str = Depends(admin_only)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code = 404, detail = "Book not found")
    db.delete(book)
    db.commit()
    return book



