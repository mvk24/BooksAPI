---
 
✅ README.md — Book Management API with FastAPI
 
# 📘 Book Management API with FastAPI
 
This is a complete backend project for managing books using **FastAPI**. It covers RESTful API operations, Swagger documentation, HTML form integration (Jinja2), query/path parameters, validation, and custom error handling.
 
---
 
## 🛠️ Requirements
 
```bash
pip install fastapi uvicorn jinja2
 
 
---
 
🚀 Project Structure
 
project/
│
├── main.py
├── templates/
│   └── book_form.html
├── static/ (optional)
│
└── README.md
 
 
---
 
📡 API Endpoints
 
➕ Add Book (JSON)
 
POST /books/
 
Body: JSON
 
Validations: Unique id or title
 
Returns: Added book object or 400 error
 
 
 
---
 
📄 Get All Books
 
GET /books/
 
Returns: List of all books
 
 
 
---
 
🔍 Get Book by ID
 
GET /books/{book_id}
 
Returns: Single book or 404 error
 
 
 
---
 
🔍 Get Book by Title or Author (Query Parameter)
 
GET /books/search?title=xyz&author=abc
 
Returns: Matching book or 404
 
title is marked as deprecated
 
 
 
---
 
✏️ Update Book
 
PUT /books/{book_id}
 
Updates: Entire book record
 
Returns: Updated object or 404
 
 
 
---
 
❌ Delete Book by ID
 
DELETE /books/{book_id}
 
Deletes: Book from DB
 
Returns: Success or 404
 
 
 
---
 
🌐 HTML Form Integration (Jinja2)
 
📄 Show Form UI
 
GET /form-ui
 
Returns: HTML form to add book using book_form.html Jinja2 template
 
 
✅ Submit Book via HTML Form
 
POST /form-ui
 
Form Data: id, title, author, yop, genre, description, price
 
Validations:
 
Unique id or title check
 
Optional: yop, description
 
 
Returns: Redirect to form with success or error message
 
 
 
---
 
⚙️ Special Features
 
✅ @Query with deprecated=True on title
 
✅ @Form(...) input via HTML
 
✅ Dynamic Jinja2 template rendering
 
✅ Duplicate book validation (by ID or title)
 
✅ Redirect after form submission
 
✅ Manual HTMLResponse for errors
 
✅ FastAPI Swagger UI with examples
 
✅ Error code consistency: 400, 404, 422
 
 
 
---
 
🧪 Testing
 
🔁 Run the API:
 
uvicorn main:app --reload
 
📂 Visit:
 
Swagger: http://localhost:8000/docs
 
Redoc: http://localhost:8000/redoc
 
Form UI: http://localhost:8000/form-ui
 
 
 
---
 
📝 Notes
 
FastAPI can use Jinja2 just like Flask or Django for server-side HTML rendering.
 
Swagger UI form inputs may show "data type" as initial value — can't fully override this without client-side JavaScript.
 
Placeholder text for HTML input was used to replace default data type values.
 
 
 
---
 
📌 TODO / Optional Enhancements
 
[ ] Persist data in DB (e.g., SQLite, PostgreSQL)
 
[ ] Add update form UI
 
[ ] Handle file/image uploads (e.g., book cover)
 
[ ] Add login/auth for form access
 
 
 
---
 