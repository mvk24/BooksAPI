
# FastAPI Book Management API with Authentication and Role-Based Access
 
A full-featured Book Management API built using **FastAPI**, supporting CRUD operations, relational user-book mapping, authentication (JWT), and role-based access control (Admin/User). The project follows a **modular structure** and uses **SQLAlchemy ORM** with a real **PostgreSQL/MySQL** backend (configurable).
 
## 📌 Features
 
### 🧾 Book Management
- Create, Read, Update, Delete (CRUD) operations for books.
- Each book is linked to a user (book owner).
- Advanced schema handling using Pydantic models with field validations.
- Optional and required fields clearly separated.
- Books owned by users are visible based on login.
- Role-based access: only Admins can delete or update any book.
 
### 👥 User Management
- Create new users with hashed passwords.
- JWT-based authentication.
- Secure login and token generation.
- Users can only modify their own books unless they are Admin.
- Get user profile, books, and full info.
 
### 🔐 Role-Based Access Control
- Roles supported: `admin`, `user`
- Admins can access additional endpoints.
- Role check integrated with `Depends`.
 
### ⚙️ Tech Stack
 
- **FastAPI**
- **SQLAlchemy ORM**
- **Pydantic**
- **Alembic** (for migrations)
- **PostgreSQL/MySQL** (DB-agnostic)
- **JWT** (OAuth2 PasswordBearer)
- Modular folder structure (models, routers, schemas, utils, db, etc.)
 
## 📂 Project Structure
 
project/ 
│ ├── app/ 
│   ├── main.py 
│   ├── database.py 
│   ├── db.py 
│   ├── models/ 
│   ├── routers/ 
│   ├── schemas/ 
│   └── utils/ 
│ ├── alembic/ 
│   ├── versions/ 
│   └── env.py 
│ ├── tests/                # (To be implemented next) │ ├── requirements.txt └── README.md
 
## 🔐 Authentication Flow
 
1. User registers with username & password.
2. Password is hashed using `bcrypt`.
3. Login generates JWT token.
4. Token used in header: `Authorization: Bearer <token>`
5. Protected routes require valid token.
 
## ⚖️ Role-Based Access
 
- Each user is assigned a role (`admin` or `user`).
- Admin-only endpoints are protected via dependency injection and custom logic.
 
## 📈 Coming Next
 
- Automated testing with `pytest`
- DB testing using a **test database session override**
- Test user and book setup/teardown using fixtures
 
---
 
## 🚀 Run the App
 
```bash
uvicorn app.main:app --reload
 
🧪 Test the API
 
Visit Swagger: http://127.0.0.1:8000/docs
 
Use JWT token in "Authorize" button to test secure endpoints.
 
 
---
 