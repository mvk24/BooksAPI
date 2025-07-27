---
 
📘 Book Management API (FastAPI)
 
A simple Book Management REST API built using FastAPI, demonstrating CRUD operations, filtering, enum usage, and path operation metadata.
 
 
---
 
🚀 How to Run the Project
 
1. Install FastAPI and Uvicorn:
 
pip install fastapi uvicorn
 
 
2. Run the server:
 
uvicorn main:app --reload
 
 
3. Open in browser:
 
Swagger UI: http://localhost:8000/docs
 
ReDoc: http://localhost:8000/redoc
 
 
 
 
 
---
 
📚 API Endpoints
 
Method	Endpoint	Description	Tags
 
GET	/books	Get all books	Books
GET	/books/{book_id}	Get a book by ID	Books
POST	/books	Add a new book	Books
PUT	/books/{book_id}	Update a book by ID	Books
DELETE	/books/{book_id}	Delete a book by ID	Books
GET	/books/first	Get the first book	Books
GET	/books/filter?author=...&title=...	Filter books by author/title	Books
GET	/books/genre/{genre}	Get books by genre	Books
 
 
 
---
 
🧾 Book Schema
 
{
  "id": 1,
  "title": "Gen AI",
  "author": "Varun M",
  "YOP": 2025,
  "description": "Intro to Gen AI",
  "price": 500,
  "genre": "tech"
}
 
 
---
 
📥 Example Requests & Responses
 
✅ Add a Book (POST /books)
 
Request Body
 
{
  "id": 1,
  "title": "FastAPI in Action",
  "author": "Varun M",
  "YOP": 2025,
  "description": "Learning FastAPI step by step",
  "price": 499,
  "genre": "tech"
}
 
Response
 
{
  "id": 1,
  "title": "FastAPI in Action",
  "author": "Varun M",
  "YOP": 2025,
  "description": "Learning FastAPI step by step",
  "price": 499,
  "genre": "tech"
}
 
 
---
 
🔍 Get All Books (GET /books)
 
Response
 
[
  {
    "id": 1,
    "title": "FastAPI in Action",
    "author": "Varun M",
    "YOP": 2025,
    "description": "Learning FastAPI step by step",
    "price": 499,
    "genre": "tech"
  }
]
 
 
---
 
✏️ Update a Book (PUT /books/1)
 
Request Body
 
{
  "id": 1,
  "title": "Updated Title",
  "author": "Varun M",
  "YOP": 2026,
  "description": "Updated description",
  "price": 599,
  "genre": "tech"
}
 
Response
 
{
  "id": 1,
  "title": "Updated Title",
  "author": "Varun M",
  "YOP": 2026,
  "description": "Updated description",
  "price": 599,
  "genre": "tech"
}
 
 
---
 
❌ Delete a Book (DELETE /books/1)
 
Response
 
{
  "success": "Book deleted successfully.",
  "book": {
    "id": 1,
    "title": "FastAPI in Action",
    "author": "Varun M",
    "YOP": 2025,
    "description": "Learning FastAPI step by step",
    "price": 499,
    "genre": "tech"
  }
}
 
 
---
 
🔎 Filter by Author or Title (GET /books/filter?author=Varun)
 
Response
 
[
  {
    "id": 1,
    "title": "FastAPI in Action",
    "author": "Varun M",
    "YOP": 2025,
    "description": "Learning FastAPI step by step",
    "price": 499,
    "genre": "tech"
  }
]
 
 
---
 
🧠 Technologies Used
 
Python
 
FastAPI
 
Pydantic
 
Uvicorn
 
 
 
---
 
🏷 Path Metadata Tags
 
All routes use:
 
tags=["Books"]
 
summary, description, and response_description for improved Swagger docs.
 
 
 
---

 