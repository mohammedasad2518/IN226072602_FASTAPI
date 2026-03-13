# FastAPI Assignments

This repository contains backend assignments built using FastAPI as part of an internship program.  
Each assignment focuses on implementing REST API concepts and backend logic using Python.

---

## Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn

---

## Topics Covered

The assignments in this repository include concepts such as:

- REST API development
- FastAPI routing
- GET, POST, and PATCH requests
- Path parameters
- Query parameters
- Request validation using Pydantic

---

## Requirements

Project dependencies are listed in the `requirements.txt` file.

Main dependencies:

- fastapi
- uvicorn
- pydantic

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mohammedasad2518/IN226072602_FASTAPI.git
```

---

### 2. Create a Virtual Environment

python -m venv venv

Activate the environment:

**Windows**

venv\Scripts\activate

**Mac / Linux**

source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

## Running the API

Navigate to any assignment folder and run:

uvicorn main:app --reload

Example:

cd assignment1 uvicorn main:app --reload

The API will start at:

http://127.0.0.1:8000

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

---

## Author

**Mohammed Asad**
