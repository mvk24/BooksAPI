---
 
Book API with Authentication - FastAPI Project
 
 
---
 
Project Overview
 
This is a REST API for managing books and users with secure authentication and role-based access control. It uses:
 
FastAPI for the API framework
 
SQLite as the database (can be swapped)
 
SQLAlchemy ORM for DB interaction
 
JWT tokens for authentication with OAuth2 password flow
 
Role-based authorization (admin vs user)
 
Unit testing with pytest and test DB isolation
 
 
 
---
 
Features
 
User signup & login with JWT token issuance
 
Admin-only book CRUD operations
 
Admin-only user management
 
Secure password hashing with bcrypt
 
API docs with Swagger UI auto-generated
 
Unit tests covering core endpoints
 
 
 
---
 
Project Structure
 
.
├── app/
│   ├── main.py                 # FastAPI app initialization & middleware
│   ├── database.py             # DB engine, session, Base
│   ├── db.py                   # DB dependency override function
│   ├── models/
│   │   ├── book_model.py       # Book ORM model
│   │   └── user_model.py       # User ORM model
│   ├── schemas/
│   │   ├── book_schema.py      # Book Pydantic schemas
│   │   ├── user_schema.py      # User Pydantic schemas
│   │   └── token_schema.py     # Token schema for login response
│   ├── routers/
│   │   ├── book_router.py      # Book endpoints (admin only)
│   │   ├── user_router.py      # User endpoints (admin only)
│   │   └── auth_router.py      # Authentication (signup/login)
│   ├── utils/
│   │   ├── auth.py             # Password hashing/verification
│   │   └── token.py            # JWT token creation & validation
│   └── dependencies/
│       └── roles.py            # Role-based access dependencies
├── tests/
│   ├── conftest.py             # Pytest fixtures, test DB setup
│   └── test_books.py           # Unit tests for books
├── books.db                    # SQLite DB file (dev)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
 
 
---
 
Setup & Running Locally
 
1. Clone repo:
 
 
 
git clone <your-repo-url>
cd <your-repo-folder>
 
2. Create & activate virtualenv:
 
 
 
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
 
3. Install dependencies:
 
 
 
pip install -r requirements.txt
 
4. Run FastAPI server:
 
 
 
uvicorn app.main:app --reload
 
5. Open http://localhost:8000/docs to access Swagger UI docs.
 
 
 
 
---
 
Authentication Flow
 
 
---
 
Signup (Register User)
 
Endpoint: POST /signup/
 
Request JSON:
 
 
{
  "username": "user1",
  "email": "user1@example.com",
  "password": "securepassword"
}
 
What happens:
 
Password is hashed before storing in DB.
 
User role defaults to "user".
 
User is saved to database.
 
JWT access token is generated and returned.
 
 
Response:
 
 
{
  "access_token": "<jwt_token>",
  "token_type": "bearer",
  "user": {
    "id": 2,
    "username": "user1",
    "email": "user1@example.com",
    "role": "user"
  }
}
 
 
---
 
Login (Get Token)
 
Endpoint: POST /login/
 
Request JSON:
 
 
{
  "username": "user1",
  "password": "securepassword"
}
 
What happens:
 
Username & password verified.
 
If valid, JWT token is issued.
 
Otherwise, 401 Unauthorized error returned.
 
 
Response:
 
 
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
 
 
---
 
How to Use the Token
 
For any protected route, send HTTP header:
 
 
Authorization: Bearer <jwt_token>
 
 
---
 
API Endpoints
 
 
---
 
Book Routes (Admin only)
 
All require Authorization header with admin token.
 
Method	Path	Description	Request Body	Response
 
POST	/books/	Create a new book	BookCreate schema (JSON)	Created book object
GET	/books/	Get all books	None	List of books
GET	/books/{id}	Get book by ID	None	Single book object
PUT	/books/{id}	Update a book	BookUpdate schema (JSON)	Updated book object
DELETE	/books/{id}	Delete a book	None	Success message
 
 
 
---
 
User Routes (Admin only)
 
Method	Path	Description	Request Body	Response
 
GET	/users/	List all users	None	List of users
GET	/users/{id}	Get user by ID	None	Single user object
POST	/users/	Create a new user	UserCreate schema (JSON)	Created user object
PUT	/users/{id}	Update a user	UserUpdate schema (JSON)	Updated user object
DELETE	/users/{id}	Delete a user	None	Success message
 
 
 
---
 
Auth Routes (Public)
 
Method	Path	Description	Request Body	Response
 
POST	/signup/	Register new user	UserSignup schema (JSON)	JWT token + User info
POST	/login/	User login	Login schema (JSON)	JWT token
 
 
 
---
 
Example Usage: Creating a Book
 
1. Signup or login to get a token.
 
 
2. Send POST /books/ with this JSON:
 
 
 
{
  "title": "My First Book",
  "author": "John Doe",
  "genre": "Fiction",
  "yop": 2023,
  "description": "A thrilling story",
  "price": 15.99
}
 
Include HTTP header:
 
Authorization: Bearer <your_jwt_token>
 
3. Response returns the created book object.
 
 
 
 
---
 
Testing
 
Run all tests with:
 
 
pytest -v
 
Tests use an in-memory SQLite DB and override real DB connection.
 
Includes tests for book creation and retrieval.
 
You can add tests for user routes and auth similarly.
 
 
 
---
 
Notes on Authentication & Authorization
 
Passwords hashed securely using bcrypt.
 
JWT tokens encode user id and role.
 
Dependency overrides in FastAPI enforce role restrictions (admin vs user).
 
Admin users can manage books and users.
 
Normal users can only signup/login.
 
 
 
---
 
Deployment (Basic Overview)
 
1. Use production server like uvicorn or gunicorn with multiple workers.
 
 
2. Configure environment variables for secrets and DB connection.
 
 
3. Use cloud services like AWS EC2, Heroku, DigitalOcean, or managed platforms.
 
 
4. Secure the app with HTTPS and proper CORS settings.
 
 
5. Use Docker for containerized deployment (optional).
 
 
6. Automate migrations and backups as needed.
 
 
 
 
---
 
Summary
 
This project covers a full, secure backend API for managing books and users with JWT-based authentication and role-based access. The README provides setup, usage, testing, and deployment basics.
 
 
---
 