
 # 📘 FastAPI Book Management API
 
A simple RESTful API built with FastAPI for managing a list of books. This API supports CRUD operations, path parameters, and filtering using query parameters.
 
---
 
## 🚀 How to Run
 
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
 
2. Start the server:
 
uvicorn main:app --reload
 
 
3. Open the interactive Swagger UI:
 
http://127.0.0.1:8000/docs
 
 
 
 
---
 
📚 Features Implemented
 
✅ 1. Add a New Book
 
Endpoint: POST /books
 
Request Body:
 
{
  "id": 1,
  "title": "Inferno",
  "author": "Dan Brown",
  "description": "Thriller fiction"
}
 
 
 
---
 
✅ 2. Get All Books
 
Endpoint: GET /books
 
Returns: List of all added books.
 
 
 
---
 
✅ 3. Get Book by ID
 
Endpoint: GET /books/{book_id}
 
Path Parameter: book_id (integer)
 
Returns: Book with matching ID.
 
 
 
---
 
✅ 4. Update a Book
 
Endpoint: PUT /books/{book_id}
 
Path Parameter: book_id (integer)
 
Request Body: Updated book object.
 
Returns: Success message with updated book.
 
 
 
---
 
✅ 5. Delete a Book
 
Endpoint: DELETE /books/{book_id}
 
Path Parameter: book_id (integer)
 
Returns: Deleted book details.
 
 
 
---
 
✅ 6. Filter Books by Author and/or Title (Query Parameters)
 
Endpoint: GET /books/filter
 
Query Parameters:
 
author (optional)
 
title (optional)
 
 
Examples:
 
/books/filter → Returns all books
 
/books/filter?author=Dan Brown → Filters by author
 
/books/filter?title=Inferno → Filters by title
 
/books/filter?author=Dan Brown&title=Inferno → Filters by both
 
 
Returns: Filtered list based on query parameters
 
 
 
---
 
🛠️ Upcoming Features
 
✅ Handling nested request bodies (e.g. with tags, genres)
 
✅ Validation & custom error messages
 
⏳ Pagination and sorting
 
⏳ Persistent storage (e.g. SQLite or PostgreSQL)
 
 
 
---
 
📌 Notes
 
All filtering is case-insensitive
 
Proper error handling using HTTPException
 
Uses Pydantic models for data validation
 
 
 
---
 
📎 Author
 
Built by Varun M
 
---

 