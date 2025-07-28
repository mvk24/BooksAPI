---
 
# 📚 FastAPI Book Management API
 
A simple Book Management REST API built using FastAPI, demonstrating core concepts such as CRUD operations, path and query parameters, validation, tagging, documentation, and more.
 
---
 
## 🚀 Run the Application
 
```bash
uvicorn main:app --reload
 
 
---
 
📌 Endpoints Summary
 
Method	Endpoint	Description
 
GET	/books	Get all books
GET	/books/{book_id}	Get a single book by ID
GET	/books/first	Get the first book
GET	/books/filter	Filter books by author/title
GET	/books/genre/{genre}	Get books by genre
POST	/books	Add a new book
PUT	/books/{book_id}	Update a book by ID
DELETE	/books/{book_id}	Delete a book by ID
 
 
 
---
 
📘 GET /books
 
Get all books in the system.
 
✅ Example Response
 
[
  {
    "id": 1,
    "title": "Python Basics",
    "author": "John Doe"
  }
]
 
 
---
 
📘 GET /books/{book_id}
 
Get a single book using its ID.
 
🔧 Path Parameter
 
Name	Type	Description
 
book_id	int	ID of the book
 
 
❌ Errors
 
404 Not Found – If no book is found.
 
 
 
---
 
📘 GET /books/first
 
Returns the first book in the collection.
 
❌ Errors
 
400 Bad Request – If no books exist.
 
 
 
---
 
📘 GET /books/filter
 
Filter books by author and/or title.
 
🔖 Tags
 
Books
 
📝 Summary
 
List of Filtered Books
 
📄 Description
 
This endpoint allows filtering of the book list based on:
 
Author name (Author_Name)
 
Book title (book_title or legacy title, which is deprecated)
 
 
 
---
 
🔧 Query Parameters
 
Name	Type	Required	Description
 
Author_Name	string	No	Filter by book author (case-insensitive)
book_title	string	No	Filter by book title (preferred parameter)
title	string	No	(Deprecated) Use book_title instead
 
 
 
---
 
📥 Example Request URLs
 
Get all books:
 
GET /books/filter
 
Filter by author:
 
GET /books/filter?Author_Name=John
 
Filter by book_title:
 
GET /books/filter?book_title=Python
 
Filter by deprecated title:
 
GET /books/filter?title=Python
 
Filter by both:
 
GET /books/filter?Author_Name=Jane&book_title=Advanced
 
 
📤 Example Response
 
[
  {
    "id": 1,
    "title": "Python Basics",
    "author": "John Doe"
  }
]
 
 
---
 
📘 GET /books/genre/{genre}
 
Get all books matching a genre.
 
🔧 Path Parameter
 
Name	Type	Description
 
genre	str	Genre of the book
 
 
 
---
 
➕ POST /books
 
Add a new book.
 
📥 Example Request
 
{
  "id": 3,
  "title": "New Book",
  "author": "Alice"
}
 
📤 Example Response
 
{
  "id": 3,
  "title": "New Book",
  "author": "Alice"
}
 
 
---
 
✏️ PUT /books/{book_id}
 
Update a book by ID.
 
📥 Example Request
 
{
  "id": 3,
  "title": "Updated Title",
  "author": "Updated Author"
}
 
📤 Example Response
 
{
  "id": 3,
  "title": "Updated Title",
  "author": "Updated Author"
}
 
❌ Errors
 
404 Not Found – If book not found.
 
 
 
---
 
❌ DELETE /books/{book_id}
 
Delete a book by ID.
 
🔧 Path Parameter
 
Name	Type	Description
 
book_id	int	ID of the book
 
 
📤 Example Response
 
{
  "Success": "Book deleted successfully.",
  "book": {
    "id": 3,
    "title": "Updated Title",
    "author": "Updated Author"
  }
}
 
 
---
 
🔖 Tags & Metadata
 
All endpoints are grouped under the tag: "Books"
 
Some parameters use:
 
alias (e.g., Author_Name instead of author)
 
deprecated (e.g., title)
 
 
 
 
---
 
🏁 Author
 
Built with ❤️ using FastAPI
Maintained by Varun M
 
 
---
 

 