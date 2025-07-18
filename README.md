<!-- # FastAPI Book API 📚
 
A simple CRUD API using FastAPI and Pydantic.
 
## Features
 
- Add a book ✅
- Get list of books ✅
- Delete a book ✅
 
## How to Run
 
1. Install dependencies:
 
```bash
pip install -r requirements.txt


2. Run the server:

uvicorn main:app --reload


3. Open your browser:

http://127.0.0.1:8000/docs -->


---
 
# 📚 FastAPI Books CRUD API (In-Memory)
 
This is a beginner-friendly **CRUD API** built with **FastAPI** using **in-memory storage** (no database yet). It allows users to **create, view, update, and delete books**.
 
---
 
## 🚀 Features
 
- ✅ Add a new book
- ✅ Get all books
- ✅ Get a book by ID
- ✅ Delete a book by ID
- ✅ Update a book by ID
- ❌ No database yet — uses an in-memory list
- 🧪 Testable with Swagger UI
 
---
 
## 🧰 Tech Stack
 
- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn** (for running the server)
 
---
 
## 📦 Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/your-username/BooksAPI.git
cd BooksAPI
 
2. Create Virtual Environment
 
python -m venv venv
 
3. Activate Virtual Environment
 
# Windows
.\venv\Scripts\activate
 
# Mac/Linux
source venv/bin/activate
 
4. Install Requirements
 
pip install fastapi uvicorn
 
 
---
 
▶️ Running the App
 
uvicorn main:app --reload
 
Visit: http://127.0.0.1:8000/docs
This opens the interactive Swagger UI to test all APIs.
 
 
---
 
🛠️ API Endpoints
 
➕ Create a Book
 
POST /books
 
Request Body:
 
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "description": "Description of the book"
}
 
 
---
 
📖 Get All Books
 
GET /books
 
 
---
 
🔍 Get Book by ID
 
GET /books/{book_id}
 
 
---
 
✏️ Update a Book by ID
 
PUT /books/{book_id}
 
Request Body:
 
{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author",
  "description": "Updated description"
}
 
 
---
 
❌ Delete a Book by ID
 
DELETE /books/{book_id}
 
 
---
 
📁 File Structure
 
BooksAPI/
├── main.py            # FastAPI app with all routes
├── README.md          # You're reading it
├── venv/              # Virtual environment (optional in .gitignore)
 
 
---
 
📌 Notes
 
This project does not use a database. All book records will reset when the server restarts.
 
Perfect for FastAPI beginners to understand the basics of CRUD.
 
 
 
---
 
🌟 Future Improvements
 
🔐 Add authentication with JWT
 
💾 Use SQLite or PostgreSQL
 
🔄 Add pagination & filtering
 
📦 Dockerize the app
 
 
 
---
 
🙌 Acknowledgements
 
FastAPI Documentation
 
Pydantic Documentation
 
 
---