# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build a basic REST API using FastAPI. In this assignment, you will create API endpoints, validate request data, and return clear JSON responses for a simple student-friendly app.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Build a FastAPI application that exposes endpoints for checking API status and managing a small in-memory collection of books.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Implement a `GET /` endpoint that returns a welcome JSON message.
- Implement a `GET /health` endpoint that returns `{ "status": "ok" }`.
- Store books in an in-memory list with fields: `id`, `title`, and `author`.
- Implement `GET /books` to return all books.


### 🛠️ Add Create and Search Features

#### Description
Extend the API so users can add new books and fetch a specific book by ID. Ensure data is validated and error responses are meaningful.

#### Requirements
Completed program should:

- Use a Pydantic model for validating incoming book data.
- Implement `POST /books` to add a new book and return the created book.
- Implement `GET /books/{book_id}` to return one book by ID.
- Return a 404 error when a requested book ID does not exist.
- Include at least one example request/response in comments or a short markdown code block.

Example request/response:

```text
POST /books
{
  "id": 3,
  "title": "Python for Teens",
  "author": "A. Smith"
}

201 Created
{
  "id": 3,
  "title": "Python for Teens",
  "author": "A. Smith"
}
```