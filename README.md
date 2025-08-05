---
 
✅ README.md – FastAPI Book Management API with JWT Authentication
 
# 📚 FastAPI Book Management API with JWT Authentication
 
A complete backend application built using **FastAPI** that provides:
 
- Full CRUD operations for **Books**
- Full CRUD operations for **Users**
- **JWT-based Authentication** (Login only)
- Modular project structure for scalability and clarity
 
---
 
## 🛠️ Tech Stack
 
- **FastAPI**: Web framework
- **Pydantic**: Data validation and serialization
- **SQLAlchemy**: ORM for database
- **SQLite**: Default database (easily switchable)
- **bcrypt + passlib**: Password hashing
- **Python-Jose**: JWT token handling
- **Uvicorn**: ASGI server
 
---
 
## 📁 Project Structure
 
```bash
.
├── main.py
├── database/
│   ├── database.py        # DB engine, Base, SessionLocal
│   └── db.py              # get_db dependency
├── models/
│   ├── book_model.py      # Book SQLAlchemy model
│   └── user_model.py      # User SQLAlchemy model
├── schemas/
│   ├── book_schema.py     # Pydantic models for Book
│   └── user_schema.py     # Pydantic models for User
├── routers/
│   ├── book_router.py     # Routes for Book CRUD
│   ├── user_router.py     # Routes for User CRUD
│   └── auth_router.py     # Route for Login
├── utils/
│   ├── auth.py            # Authentication logic
│   └── token.py           # JWT generation/verification
├── requirements.txt
└── README.md
 
 
---
 
🧑‍💻 Features
 
🔐 Authentication
 
POST /auth/login: Login with username & password to receive JWT token
→ Token returned in { "access_token": ..., "token_type": "bearer" }
→ Token type is "bearer" used in Authorization: Bearer <token> header
 
 
📘 Book APIs
 
GET /books/ → Get all books
 
GET /books/{id} → Get a book by ID
 
POST /books/ → Add a new book
 
PUT /books/{id} → Update a book
 
DELETE /books/{id} → Delete a book
 
 
👤 User APIs
 
GET /users/ → Get all users
 
GET /users/{id} → Get a user by ID
 
POST /users/ → Register a new user (password is hashed)
 
PUT /users/{id} → Update user info
 
DELETE /users/{id} → Delete a user
 
 
 
---
 
🧾 Usage
 
1. 📦 Install dependencies
 
pip install -r requirements.txt
 
2. ⚙️ Run the app
 
uvicorn main:app --reload
 
3. 🌐 Open Swagger UI
 
Visit: http://127.0.0.1:8000/docs
Try out the endpoints with built-in testing interface.
 
 
---
 
🔐 Authentication Flow (JWT)
 
1. Register a user using /users/ POST
 
 
2. Login via /auth/login with username and password
 
 
3. Get back:
 
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
 
 
4. Use it for protected routes in headers:
 
Authorization: Bearer <access_token>
 
 
 
Note: Currently, login is implemented, but routes are not protected with token yet.
 
 
---
 
⚠️ Notes
 
Passwords are stored in hashed form using bcrypt.
 
JWT Secret key and expiry time are defined in utils/token.py.
 
Token is generated with user’s ID and username.
 
Currently only login (/auth/login) is implemented; registration is handled via /users/ POST.
 
 
 
---
 
📝 Future Enhancements
 
✅ Secure all routes with JWT token using OAuth2 dependency
 
🔐 Add role-based permissions
 
📤 Pagination & filtering in list endpoints
 
🧪 Unit testing
 
🐳 Dockerization
 
 
 
---
 
📌 License
 
This project is for learning/demo purposes. Customize as needed.
 