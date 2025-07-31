# 📚 Book Management API – FastAPI Project
 
This project is a backend API for managing a collection of books. It demonstrates complete CRUD operations using FastAPI, SQLAlchemy, and Pydantic.
 
---
 
## ✅ Features Implemented
 
### 1. **Create Book**
- **Via Swagger UI (JSON body)**
- **Via HTML Form (using Jinja2 template)**
- Auto-generates `id` using SQLAlchemy `Integer, primary_key=True, index=True`
- Returns `BookOut` schema with all fields including `id`
 
### 2. **Read Books**
- Returns list of all books in JSON format
- Response uses `BookOut` schema
- The `id` appears in the response (usually last due to JSON rendering order in browser/Swagger UI)
 
### 3. **Update Book**
- `PUT /books_db/{book_id}` updates a book's details by ID
 
### 4. **Delete Book**
- `DELETE /books_db/{book_id}` removes a book from the DB
 
---
 
## 📁 Project Structure
 
 
├── main.py 
├── models.py 
├── schemas.py
├── database.py
├── templates/
    └── add_book.html
└── README.md
 
---
 
## 🔧 Tech Stack
 
- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy**
- **SQLite** (can be swapped with PostgreSQL/MySQL)
- **Jinja2 (optional)** – for HTML form rendering
 
---
 
## 📥 Sample JSON for POST
 
```json
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "genere": "Fiction",
  "yop": 1988,
  "description": "A philosophical book",
  "price": 299.99
}
 
 
---
 
📤 Sample Response
 
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "genere": "Fiction",
  "yop": 1988,
  "description": "A philosophical book",
  "price": 299.99,
  "id": 1
}
 
> 🔸 Note: Even if id is defined first in your schema, some tools render it last.
 
 
 
 
---
 
🧪 How to Run
 
uvicorn main:app --reload
 
Then go to: http://127.0.0.1:8000/docs
 
 
---
 
📌 To Do Next
 
Add authentication (login, token, etc.)
 
Add search or filter functionality
 
Connect to PostgreSQL/MySQL (optional)
 
Containerize using Docker
 
Add unit tests
 
 
 
---
 
🧠 Learning Summary (Till Today)
 
✅ Basic FastAPI setup
 
✅ Path and query parameters
 
✅ POST, GET, PUT, DELETE routes
 
✅ SQLAlchemy ORM and models
 
✅ Pydantic models with from_orm and model_config
 
✅ HTML form integration using Jinja2
 
✅ Handling of auto-generated fields like id
 

 ---
  Built by Varun M
 ---
 
 