
✅ FINAL README.md (Full Project Demo)
 
# 📚 FastAPI Bookstore API with JWT Auth
 
A modular **FastAPI backend** project with:
 
- User authentication (JWT-based, role-protected)
- CRUD operations for managing books
- Modular file structure (routers, models, schemas, utils)
- SQLAlchemy + Pydantic integration
- Swagger UI for easy testing
 
---
 
## 🚀 Tech Stack
 
- **FastAPI** – High-performance Python web framework
- **SQLAlchemy** – ORM for database interactions
- **SQLite / PostgreSQL / MySQL** – DB support via SQLAlchemy
- **Pydantic** – For schema validation
- **JWT (PyJWT)** – For secure user authentication
- **bcrypt** – Password hashing
 
---
 
## 🎯 Features
 
### 🔐 Authentication
- User Signup (register)
- User Login (JWT access token only)
- Hashed password storage
- Role-based access (admin/user)
 
### 📘 Book Management (CRUD)
- Add a new book
- Get all books
- Get book by ID
- Update book
- Delete book
 
### 👤 User Info & RBAC
- Get current user
- Admin-only endpoints
 
---
 
## 📁 Project Structure
 
. ├── main.py 
  ├── database/
  │   ├── database.py        # SQLAlchemy setup (engine, Base) 
  │   └── db.py              # Dependency: get_db ├── models/ 
  │   └── user.py            # User + Book DB Models 
  ├── schemas/ 
  │   └── user_schema.py     # Pydantic schemas for User & Book 
  ├── routers/ 
  │   ├── auth.py            # Signup & Login 
  │   ├── user.py            # Get current user, role checks 
  │   └── book.py            # CRUD routes for books 
  ├── utils/ 
  │   ├── hash.py            # Password hashing 
  │   └── token.py           # JWT encode/decode 
  ├── README.md
 
---
 
## ⚙️ Setup & Run Locally
 
### 1️⃣ Clone & Install
 
```bash
git clone <repo_url>
cd fastapi-bookstore
pip install -r requirements.txt
 
2️⃣ Run App
 
uvicorn main:app --reload
 
3️⃣ Open Swagger UI
 
Visit: http://127.0.0.1:8000/docs
 
 
---
 
📌 API Endpoints
 
🔐 Auth
 
Method	Endpoint	Description
 
POST	/signup	Register new user
POST	/login	Login, get token
 
 
📘 Books (Protected)
 
Method	Endpoint	Description
 
GET	/books	List all books
POST	/books	Add a new book
GET	/books/{id}	Get book by ID
PUT	/books/{id}	Update book
DELETE	/books/{id}	Delete book
 
 
👤 User Routes (Protected)
 
Method	Endpoint	Description
 
GET	/me	Get current user info
GET	/admin-only	Admins only endpoint
 
 
 
---
 
🔐 JWT Auth Flow
 
1. Register using /signup
 
 
2. Login at /login (returns JWT token)
 
 
3. Use Swagger UI "Authorize" button:
 
Bearer <your_access_token>
 
 
4. Now test any protected routes like /books, /me, etc.
 
 
 
 
---
 
🧪 Example Testing (cURL)
 
curl -X POST http://127.0.0.1:8000/signup -H "Content-Type: application/json" \
-d '{"username": "john", "password": "pass123", "role": "user"}'
 
curl -X POST http://127.0.0.1:8000/login -d "username=john&password=pass123"
 
 
---
 
✅ Enhancements (TODO / Optional)
 
Add Refresh Token
 
OAuth (Google, GitHub) login
 
Pagination for books
 
Unit tests with PyTest
 
Admin dashboard integration
 
 
 
---
 
🙏 Credits
 
FastAPI Docs
 
SQLAlchemy Docs
 
PyJWT
 
Community Support
 

---
 
 
 