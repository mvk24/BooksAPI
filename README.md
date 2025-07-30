---
  # 📚 FastAPI Book Management API
 
A full-featured FastAPI project to manage a collection of books with both RESTful APIs and HTML form-based submission using Jinja2.
 
---
 
## 🚀 Features
 
- ✅ Add, Update, Delete, and Get Books via API
- ✅ Input Validation using Pydantic V2
- ✅ Custom Exception Handling
- ✅ Dependency Injection
- ✅ Background Tasks
- ✅ Middleware (including custom logging middleware)
- ✅ CORS Setup
- ✅ HTML Form for adding a book using Jinja2
- ✅ Success page after form submission
- ✅ Redirects and HTML response rendering
 
---
 
## 📂 Project Structure
 
/your_project/ │ 
├── main.py                  # FastAPI app and route logic
  ├── templates/              # HTML templates for form and success page │  
    ├── add_book.html │ 
      └── success.html 
      └── README.md
 
---
 
## 🔧 Tech Stack
 
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Validation**: Pydantic V2
- **Templating**: Jinja2
 
---
 
## 📡 API Endpoints
 
### 🔹 Book Endpoints
 
| Method | Endpoint             | Description             |
|--------|----------------------|-------------------------|
| GET    | `/books`             | Get all books           |
| GET    | `/books/{book_id}`   | Get book by ID          |
| POST   | `/books`             | Add a new book          |
| PUT    | `/books/{book_id}`   | Update existing book    |
| DELETE | `/books/{book_id}`   | Delete book by ID       |
 
### 🔹 HTML Endpoints
 
| Method | Endpoint             | Description               |
|--------|----------------------|---------------------------|
| GET    | `/books/form`        | Show form to add book     |
| POST   | `/books/form-submit` | Submit book via form      |
 
---
 
## 🛠️ How to Run
 
1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn jinja2
 
2. Run the server
 
uvicorn main:app --reload
 
 
3. Visit in browser
 
Swagger Docs: http://127.0.0.1:8000/docs
 
Book Form UI: http://127.0.0.1:8000/books/form
 
 
 
 
 
---
 
📝 Notes
 
Use /docs or /redoc for Swagger-based interactive API testing.
 
HTML form handles book creation separately via POST /books/form-submit.
 
 
 
---
 
📌 Upcoming (Optional Add-ons)
 
[ ] Database integration (SQLite/PostgreSQL + SQLAlchemy)
 
[ ] User Authentication (OAuth2/JWT)
 
[ ] Pagination and Filtering
 
[ ] Dockerization
 
 
 
---
 
🙌 Author
 
Built with ❤️ by VARUN M
 
---

 