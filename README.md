
# Book API with Authentication
 
This project is a FastAPI-based RESTful API for managing books and users with authentication & authorization using OAuth2 and JWT tokens.
 
---
 
## Table of Contents
 
- [Project Structure](#project-structure)  
- [Setup and Installation](#setup-and-installation)  
- [Running the Application](#running-the-application)  
- [API Routes with Examples](#api-routes-with-examples)  
- [Testing](#testing)  
- [Technologies Used](#technologies-used)  
 
---
 
## Project Structure
 
fastapi_project/
├── main.py                  # FastAPI app entry point
├── database.py              # Database engine and Base declaration
├── db.py                    # Database session dependency (get_db)
├── models/
│   ├── book_model.py        # Book ORM model
│   └── user_model.py        # User ORM model
├── schemas/
│   ├── book_schema.py       # Book Pydantic schemas
│   ├── user_schema.py       # User Pydantic schemas
│   └── token_schema.py      # Token schema
├── routers/
│   ├── book_router.py       # Book API routes
│   ├── user_router.py       # User API routes
│   └── auth_router.py       # Authentication routes (signup/login)
├── utils/
│   ├── auth.py              # Password hashing and auth helper functions
│   └── token.py             # JWT token creation and verification
├── tests/
│   ├── conftest.py          # Pytest fixtures and dependency overrides for testing
│   ├── test_books.py        # Unit tests for Book endpoints
│   └── test_users.py        # Unit tests for User endpoints (optional)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
 
---
 
## Setup and Installation
 
1. Clone the repository:  
   ```bash
   git clone <your-repo-url>
   cd fastapi
 
2. Create and activate a virtual environment:
 
python -m venv venv
source venv/bin/activate      # Linux/Mac  
.\venv\Scripts\activate       # Windows PowerShell
 
 
3. Install dependencies:
 
pip install -r requirements.txt
 
 
4. Start the app (tables auto-created):
 
uvicorn main:app --reload
 
 
5. Open API docs at:
 
http://127.0.0.1:8000/docs
 
 
 
 
---
 
API Routes with Examples
 
All routes require authentication except signup and login. Admin role is required for book creation, update, and deletion.
 
 
---
 
Authentication Routes
 
1. Signup
 
Endpoint: POST /auth/signup
 
Description: Register a new user.
 
Input JSON:
 
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "strongpassword"
}
 
Output JSON:
 
{
  "id": 1,
  "username": "newuser",
  "email": "newuser@example.com",
  "role": "user"
}
 
 
 
---
 
2. Login
 
Endpoint: POST /auth/login
 
Description: Authenticate user and get JWT token.
 
Input (form data):
 
username=newuser
password=strongpassword
 
Output JSON:
 
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
 
 
 
---
 
User Routes (Authentication required)
 
3. Get All Users
 
Endpoint: GET /users/
 
Description: Fetch all registered users.
 
Output JSON (list):
 
[
  {
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com",
    "role": "user"
  },
  ...
]
 
 
 
---
 
4. Get User by ID
 
Endpoint: GET /users/{user_id}
 
Description: Fetch user details by ID.
 
Output JSON:
 
{
  "id": 1,
  "username": "newuser",
  "email": "newuser@example.com",
  "role": "user"
}
 
 
 
---
 
5. Update User
 
Endpoint: PUT /users/{user_id}
 
Description: Update user info (username/email).
 
Input JSON:
 
{
  "username": "updateduser",
  "email": "updated@example.com"
}
 
Output JSON: Updated user object (similar to above).
 
 
 
---
 
6. Delete User
 
Endpoint: DELETE /users/{user_id}
 
Description: Delete user by ID.
 
Output JSON:
 
{
  "detail": "User deleted successfully."
}
 
 
 
---
 
Book Routes (Authentication required, Admin only for POST/PUT/DELETE)
 
7. Create Book
 
Endpoint: POST /books/
 
Description: Add new book to the collection.
 
Input JSON:
 
{
  "title": "FastAPI Guide",
  "author": "John Doe",
  "genre": "Tech",
  "yop": 2023,
  "description": "A complete guide on FastAPI.",
  "price": 39.99
}
 
Output JSON:
 
{
  "id": 1,
  "title": "FastAPI Guide",
  "author": "John Doe",
  "genre": "Tech",
  "yop": 2023,
  "description": "A complete guide on FastAPI.",
  "price": 39.99,
  "owner_id": 1
}
 
 
 
---
 
8. Get All Books
 
Endpoint: GET /books/
 
Description: List all books.
 
Output JSON (list):
 
[
  {
    "id": 1,
    "title": "FastAPI Guide",
    "author": "John Doe",
    "genre": "Tech",
    "yop": 2023,
    "description": "A complete guide on FastAPI.",
    "price": 39.99,
    "owner_id": 1
  },
  ...
]
 
 
 
---
 
9. Get Book by ID
 
Endpoint: GET /books/{book_id}
 
Description: Fetch details of a single book.
 
Output JSON:
 
{
  "id": 1,
  "title": "FastAPI Guide",
  "author": "John Doe",
  "genre": "Tech",
  "yop": 2023,
  "description": "A complete guide on FastAPI.",
  "price": 39.99,
  "owner_id": 1
}
 
 
 
---
 
10. Update Book
 
Endpoint: PUT /books/{book_id}
 
Description: Update book details.
 
Input JSON: (same as create)
 
Output JSON: Updated book object.
 
 
 
---
 
11. Delete Book
 
Endpoint: DELETE /books/{book_id}
 
Description: Delete book by ID.
 
Output JSON:
 
{
  "detail": "Book deleted successfully."
}
 
 
 
---
 
Testing
 
Run tests with:
 
pytest -v
 
Uses a test database to isolate tests from real data.
 
Tests cover main functionality for books and users.
 
 
 
---
 
Technologies Used
 
FastAPI
 
SQLAlchemy ORM
 
SQLite (default, easily switchable)
 
Pydantic schemas
 
OAuth2 with JWT authentication
 
Pytest for automated testing
 
 
 
---
 
Notes
 
Make sure to secure your JWT secret key in production.
 
You can use the Swagger UI docs for interactive testing: /docs
 
Extend roles and permissions as needed for your project.
 
 
 
---
 
Contact
 
Open issues or pull requests for questions or contributions.
 
 
---
 
This README was created to help new developers onboard quickly and understand the project fully.
 
---
 