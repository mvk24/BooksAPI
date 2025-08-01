---
 
📘 FastAPI Book Management API
 
A backend service built with FastAPI, SQLAlchemy, and SQLite, allowing you to perform CRUD operations on a collection of books. The API includes strong validation, custom error handling, and clean integration with Swagger UI.
 
 
---
 
📂 Project Structure
 
book_api/
│
├── main.py                  # FastAPI app with routes
├── models.py                # SQLAlchemy ORM models
├── schemas.py               # Pydantic schemas with validation
├── database.py              # DB connection and session
└── requirements.txt         # Python dependencies
 
 
---
 
✅ Features
 
🔁 Full CRUD operations (Create, Read, Update, Delete)
 
✅ Strong validation with Pydantic and custom validators
 
❌ Prevents default placeholder inputs like "string", "ok", "n/a"
 
💾 SQLite database with SQLAlchemy ORM
 
🧪 Built-in Swagger UI for testing
 
🔐 Optional CORS and middleware integration
 
📦 Background tasks & Dependency injection ready (optional extensions)
 
 
 
---
 
⚙️ Setup Instructions
 
1. Clone the repo & install dependencies
 
git clone https://github.com/your-username/book-api.git
cd book-api
pip install -r requirements.txt
 
2. Run the app
 
uvicorn main:app --reload
 
3. Access Swagger UI
 
Visit http://localhost:8000/docs
 
 
---
 
🧾 API Endpoints
 
📥 Add a New Book
 
POST /books_db/
 
Body (example):
 
{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "genre": "Fiction",
  "yop": 1988,
  "description": "Spiritual journey of a shepherd",
  "price": 299.99
}
 
📚 Get All Books
 
GET /books_db/
 
🔍 Get Book by ID
 
GET /books_db/{book_id}
 
✏️ Update Book by ID
 
PUT /books_db/{book_id}
 
Body: Same as POST
 
❌ Delete Book by ID
 
DELETE /books_db/{book_id}
 
 
---
 
🛡️ Validation & Error Handling
 
Fields like title and author are mandatory.
 
Other fields (genre, description, yop, price) are optional.
 
Rejects default Swagger placeholder values like "string", "ok", "na" using Pydantic validators.
 
Proper HTTP status codes and messages on invalid input or missing data.
 
 
 
---
 
📦 Tech Stack
 
Python 3.10+
 
FastAPI
 
SQLAlchemy
 
SQLite
 
Pydantic v2.x
 
 
 
---
 
🔍 Notes
 
Use DB Browser for SQLite to inspect your books.db file if needed.
 
To reset DB, delete the books.db file and restart the app.
 
Use /books_db/cleanup endpoint (temp-only) to delete invalid books with placeholder data.
 
 
 
---
 
✅ To-Do (Optional Enhancements)
 
Authentication (JWT/OAuth2)
 
Pagination for large datasets
 
Search and filter capabilities
 
Dockerize the app
 
Migrate to PostgreSQL for production use
 
 
---
 