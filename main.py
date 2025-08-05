from fastapi import FastAPI, HTTPException, Query, Form, Request, status, Depends, Path, BackgroundTasks
from routers.book_router import router as book_router
from routers.user_router import router as user_router
from routers.auth_router import router as auth_router
from database import SessionLocal, engine, Base

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
import time


# from sqlalchemy.orm import Session
# from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates
# from pydantic import BaseModel, Field, field_validator
# from typing import List, Optional
# from db import get_db
# from enum import Enum
# import time, models.book_model as book_model, schemas.book_schema as book_schema


# Create tables if not exists
Base.metadata.create_all(bind = engine)

app = FastAPI(title = "Book API with AUTH")

# CORS Middleware
app.add_middleware(CORSMiddleware,
                   allow_origins = ["*"],
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
                   )


# MIDDLEWARE TO LOG TIME TAKEN BY DIFF REQUESTS OR PROCESS
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        print(f"[{request.method}] {request.url} completed in {process_time:.4f}s")
        return response


# Logging Middleware
app.add_middleware(LoggingMiddleware)

app.include_router(book_router)
app.include_router(user_router)
app.include_router(auth_router)


# # Dpendency: DB session Generator
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# -----------------------------------------In memory List Implementation------------------------------------------


# # JINJA 2 TEMPLATE TO ADD BOOK VIA HTML FORM
# templates = Jinja2Templates(directory = "templates")     



# # ENUM FOR VALID GENERS
# class GenereNum(str, Enum):
#     fi = "fiction"
#     sc = "science"
#     his = "history"
#     te = "tech"


# # DEFINING THE DATA MODEL WITH VALIDATION
# class Book(BaseModel):
#     id: int  # Required
#     title: str = Field(..., min_length=3, max_length=100, description="Title must be between 3-100 characters long.")
#     author: str = Field(..., min_length=3, description="Author name should be at least 3 characters.")
#     genere: str = Field(..., min_length=3, description="Genere is required.")
#     YOP: Optional[int] = None  # Optional year of publication
#     description: Optional[str] = None
#     price: float = Field(..., gt=0, description="Price must be greater than 0.")



# # Custom Validator to avoid pre filled data.
#     @field_validator('title', 'author', 'genere', 'description')
#     @classmethod
#     def reject_defalut_strings(cls, value):
#             if value.strip().lower() in ["", "string", "ok", "na", "none", "n/a"]:
#                 raise ValueError("Fields cannot be default placeholder")
#             return value






# # LOCAL IN MEMORY LIST TO STORE DEFAULT BOOK RECORDS, USER INPUT VIA SWAGGER UI ARE ACCEPTED.
# books: List[Book] = [
#     Book(id = 0, title = "Python", author = "Varun", genere = "tech", YOP = 2025, description = "Good Python Book.", price = 777),
#     Book(id = 1, title = "DSA", author = "MVK", genere = "science", description = "Good DSA Book.", price = 500.99),
#     Book(id = 2, title = "Java", author = "MVK", genere = "fiction", description = "Java best seller.", price = 600)]




# # Re-Usable dependency to fetch Book by ID
# def get_book_id(book_id: int):
#     for book in books:
#         if book.id == book_id:
#             return book
#     raise HTTPException(status_code = 404, detail = "Book not found")



# # Backgorund Task Method
# def log_book_addition(title: str):
#     with open("log.txt", "a") as log:
#         log.write(f"Book added: {title}\n")



# # TO ADD NEW BOOK
# @app.post("/books", response_model = Book, tags = ["Books"], summary = "Add a new book.", description = "Insert a new book into the In memory list.", response_description = "The book added to the system.", response_model_exclude_none = True, status_code = 201)
# def create_book(book: Book):
#     for b in books:
#         if b.id == book.id:
#             raise HTTPException(status_code = 400, detail = f"Book with ID {book.id} already exists.")
#     books.append(book)
#     return book


# # Add new Book with Logging to text file.
# @app.post("/books/", response_model = Book, tags = ["Books"], summary = "Add Book with Logging", description = "Add a nee book by Logging to the Log.txt file asynchronously.")
# def add_book(book: Book, background_tasks: BackgroundTasks):
#     for b in books:
#         if b.id == book.id:
#             raise HTTPException(status_code = 400, detail = f"Book with ID {book.id} already exists.")
#     books.append(book)
#     background_tasks.add_task(log_book_addition, book.title)
#     return book




# # CORS Setup Confirmation
# @app.get("/")
# def home():
#     return {"message": "CORS Setup succesfful."}


# # GET ALL BOOKS WITHOUT FILTERS
# @app.get("/books", tags = ["Books"], summary=  "Get all books.", description = "Retrieve a list of all available books in the memory.", response_description="List of Books in memory", response_model = List[Book], status_code = 200)
# def get_all_books():
#     return books


# # ADD NEW BOOK VIA HTML FORM USING JINJA2 TEMPLATE 
# @app.get("/form-ui", response_class = HTMLResponse)
# def book_form(request: Request):
#     return templates.TemplateResponse("book_form.html", {"request": request, "books": books})

# # POST REQUEST TO HANDLE FORM DATA FROM JINJA 2 TEMPLATE
# @app.post("/form-ui", response_class = HTMLResponse, tags = ["Books"], summary = "Add a new book using HTML Form", description = "Add new Book using HTML FORM instead of JSON Format", response_description = "The Book added")
# async def submit_form(
#     request: Request,
#     id: int = Form(...),
#     title: str = Form(...),
#     author: str = Form(...),
#     yop: Optional[int] = Form(None),
#     genere: str = Form(...),
#     description: Optional[str] = Form(...),
#     price: float = Form(...)):

#     for b in books:
#         if b.id == id or b.title.lower() == title.lower():
#             return HTMLResponse(content = f"<h3 style = 'color:red;'> Book already exists (by ID or Title). </h3><a> href = '/books/form-ui'> Go Back </a>", status_code = 400)

#     new_book = Book(id = id, title = title, author = author, yop = yop, genere = genere, description = description, price = price)
#     books.append(new_book)
#     return RedirectResponse(url = "/form-ui", status_code = status.HTTP_303_SEE_OTHER)



# # GET THE FIRST BOOK
# @app.get("/books/first", tags = ["Books"], summary = "First Book in memory list", description = "Return the first available book from the memory system", response_description = "The first book object",response_model = Book)
# def first_book():
#     if not books:
#         raise HTTPException(status_code = 404, detail = "Book not found.")
#     return books[0]
    


# # GET BOOKS BY GENERE
# @app.get("/books/genere/{genere}", response_model = List[Book], tags = ["Books"], summary = "Get Books by Genere", description = "Retrieve all books that match a specific genere using Enum", response_description = "List of Books filtered by Genere")
# def get_book_by_genere(genere: GenereNum):
#     filtered_books = [book for book in books if book.genere == genere.value]
#     if not filtered_books:
#         raise HTTPException(status_code = 404, detail = "No books found in this genere.")
#     return filtered_books




# # FILTER BOOKS BY AUTHOR & TITLE (QUERY PARAMATER)
# @app.get("/books/filter", response_model = List[Book], tags = ["Books"], summary = "List of Filtered books.", description = "Filter books by author AND/OR title using Path and Query Parameters.", response_description = "List of filtered books")
# def filter_books(
#     author: Optional[str] = Query(None, alias = "Author_Name"),
#     title: Optional[str] = Query(None, deprecated = True, description = "This parameter is deprecated. Use new paramater i.e. Book_Title"),
#     Book_Title: Optional[str] = Query(None, description = "New parameter for title") ):
#     if author is None and title is None and Book_Title is None:
#         return{"All Books": books}
    
#     search_title = Book_Title or title

#     filtered_books = books
#     if author:
#         filtered_books = [book for book in filtered_books if author.lower() in book.author.lower()]
#     if search_title:
#         filtered_books = [book for book in filtered_books if search_title.lower() in book.title.lower()]
#     return filtered_books



# # GET BOOKS BY ID ( Used Dependency Injection )
# @app.get("/books/{book_id}", response_model = Book, tags = ["Books"], summary = "Get Book by ID", description = "Fetch a single book usings its ID", response_description = "Matching Book", status_code = 200)
# def read_book(book: Book = Depends(get_book_id)):
#     return book



# # DELETE BOOKS BY ID ( PATH PARAMETER )
# @app.delete("/books/{book_id}", response_model = Book, status_code = 200, tags = ["Books"], summary = "Delete Book by ID", description = "Delete a book from the memory List using its ID", response_description = "Deleted book")
# def delete_book(book_id: int):
#         for index, book in enumerate(books):
#             if book.id == book_id:
#                 del_book = books.pop(index)
#                 return JSONResponse(content = {"Success":"Book deleted successfully.", "book": del_book.dict()})
#         raise HTTPException(status_code = 404, detail="Book not found.")
    


# # UPDATE BOOKS BY ID ( PATH PARAMETER + REQUEST BODY )
# @app.put("/books/{book_id}", response_model = Book, status_code = 200, tags = ["Books"], summary = "Update Book by ID", description = "Update the details of a specific book using its ID", response_description = "Updatated Book Object")
# def update_book(book_id: int, updated_book: Book):
#     for index, book in enumerate(books):
#         if book.id == book_id:
#             if updated_book.id != book_id and any(b.id == updated_book.id for b in books):
#                 raise HTTPException(status_code = 400, detail = "Updated ID already exists for another book. Please change the ID.")
#             books[index] = updated_book
#             return JSONResponse(content = {"message": "Book Updated Successfully", "book": updated_book.dict()})
        
#     raise HTTPException(status_code = 404, detail = "Book not found")






