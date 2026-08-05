# StarHotel API

A hotel management backend system built using **FastAPI** and **PostgreSQL**.

The project focuses on building a practical intermediate-level backend application with REST APIs, database integration, user management, hotel management, room management, booking system, and AI chatbot support.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic
* Docker
* ChromaDB
* LangChain

## Project Features

### Completed

### 1. Project Setup

* FastAPI application structure created
* Environment configuration setup
* PostgreSQL database connected
* Docker PostgreSQL container configured

### 2. Database Integration

* SQLAlchemy ORM configured
* Database connection tested
* Table creation workflow implemented

### 3. User Authentication (Simple)

* User registration API
* User login API
* Password hashing using Argon2
* No JWT/token authentication (kept simple for project scope)

### 4. API Documentation

* Swagger UI available through FastAPI Docs

```
http://127.0.0.1:8000/docs
```

## Project Structure

```
starhotel
│
├── app
│   ├── auth
│   │   └── hashing.py
│   │
│   ├── models
│   │   ├── user.py
│   │   ├── hotel.py
│   │   ├── room.py
│   │   └── booking.py
│   │
│   ├── routers
│   │   ├── auth.py
│   │   ├── hotels.py
│   │   ├── rooms.py
│   │   └── bookings.py
│   │
│   ├── schemas
│   │   └── user.py
│   │
│   ├── services
│   │   └── business logic
│   │
│   ├── database.py
│   └── main.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Running the Project

### 1. Start PostgreSQL

```bash
docker compose up -d
```

### 2. Activate Virtual Environment

Windows:

```powershell
.venv\Scripts\activate
```

### 3. Create Database Tables

```bash
python create_tables.py
```

### 4. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

## API Endpoints

### Authentication

Register User

```
POST /auth/register
```

Login User

```
POST /auth/login
```

## Future Development

* Hotel CRUD APIs
* Room management APIs
* Booking management
* Guest management
* AI chatbot integration
* Document-based hotel information search using RAG

## Project Goal

Build a practical hotel management backend system that combines traditional database operations with AI-powered features.
