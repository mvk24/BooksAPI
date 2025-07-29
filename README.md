
# 📘 Book Management API with FastAPI
 
A simple and powerful RESTful API built using **FastAPI** to manage books. This project is focused on learning FastAPI concepts like routing, models, path/query parameters, form/file handling, headers/cookies, middleware, dependency injection, and exception handling.
 
---
 
## 🚀 Features Implemented with Examples
 
### ✅ Add a Book (POST `/books`)
```python
@app.post("/books")
def add_book(book: Book):
    for b in books_db:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book already exists.")
    books_db.append(book.dict())
    return {"message": "Book added successfully"}
 

---
 
✅ Get All Books (GET /books)
 
@app.get("/books")
def get_books():
    return books_db
 
 
---
 
✅ Get Book by ID (GET /books/{book_id})
 
@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
 
 
---
 
✅ Update Book by ID (PUT /books/{book_id})
 
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books_db):
        if book["id"] == book_id:
            books_db[i] = updated_book.dict()
            return {"message": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")
 
 
---
 
✅ Delete Book by ID (DELETE /books/{book_id})
 
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books_db):
        if book["id"] == book_id:
            del books_db[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
 
 
---
 
✅ Query Parameters (GET /search)
 
@app.get("/search")
def search_books(genre: str = Query(None)):
    if genre:
        return [book for book in books_db if book.get("genre") == genre]
    return books_db
 
 
---
 
✅ Optional Fields in Request Body
 
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str] = None
 
 
---
 
✅ Middleware – Log Requests
 
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response
 
 
---
 
✅ Dependency Injection – Token Header Check for Protected Route
 
def verify_token(x_token: str = Header(...)):
    if x_token != "varun-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token Header")
 
@app.get("/secure/books", dependencies=[Depends(verify_token)])
def get_secure_books():
    return books_db
 
 
---
 
✅ Custom Exception Handling – Book Not Found
 
class BookNotFoundException(Exception):
    def __init__(self, book_id: int):
        self.book_id = book_id
 
@app.exception_handler(BookNotFoundException)
def book_not_found_handler(request: Request, exc: BookNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Book with ID {exc.book_id} not found"},
    )
 
@app.get("/custom/{book_id}")
def get_book_custom(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise BookNotFoundException(book_id)
 
 
---
 
📂 Project Structure
 
book_api/
│
├── main.py               # Main application with routes and logic
├── models.py             # Pydantic models (Book)
├── middleware/           # Custom middleware (optional)
├── README.md             # This documentation
 
 
---
 
▶️ Run the Project
 
uvicorn main:app --reload
 
Visit:
 
Swagger UI: http://127.0.0.1:8000/docs
 
ReDoc: http://127.0.0.1:8000/redoc
 
 
 
---
 
✅ Requirements
 
Python 3.9+
 
FastAPI
 
Uvicorn
 
 
Install dependencies:
 
pip install fastapi uvicorn
 
 
---
 
🧑‍💻 Author
 
Built by Varun M.
 
---
 