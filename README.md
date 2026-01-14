📝 Notes Management System
Full-Stack Application (FastAPI + Next.js)

A production-ready full-stack Notes Management System with secure authentication, protected APIs, and versioned notes.
Built to demonstrate real-world backend–frontend integration, JWT authentication, database handling, and cloud deployment.

🚀 Live Applications
🌐 Frontend (Vercel)
https://notes-frontend-t8qm.vercel.app/

⚙️ Backend API (Render)
https://notes-api-f8qj.onrender.com

📘 API Documentation
https://notes-api-f8qj.onrender.com/docs

🎯 Project Objective

The goal of this project is to build a realistic, industry-style full-stack application where:

Users can securely register & log in

Only authenticated users can create and manage notes

Each note maintains version history

Frontend and backend communicate via secure REST APIs

The system is deployed and accessible publicly

🧠 Key Features
🔐 Authentication & Security

User registration with hashed passwords

JWT-based login system

Protected routes using Bearer tokens

Secure password hashing (bcrypt)

📝 Notes Management

Create notes

Fetch notes belonging to the logged-in user

Prevent unauthorized access

Version history support for notes

🌐 Frontend Integration

Fully connected Next.js frontend

Token-based API calls

Error-safe fetch handling

Clean UI for login, register, and notes

☁️ Cloud Deployment

Backend deployed on Render

Frontend deployed on Vercel

CORS configured for dynamic Vercel domains

🛠️ Tech Stack
Backend

FastAPI

SQLAlchemy

SQLite / PostgreSQL

Pydantic

JWT (python-jose)

Uvicorn

bcrypt

Frontend

Next.js

React

JavaScript

CSS

Fetch API

Deployment

Render (Backend)

Vercel (Frontend)

🧱 System Architecture
[ Next.js Frontend ]
        |
        |  HTTPS (JWT)
        |
[ FastAPI Backend ]
        |
        |
[ SQL Database ]

Flow Summary:

User registers or logs in

Backend issues JWT token

Frontend stores token

Token sent in Authorization header

Backend validates user

User accesses protected APIs

📂 Backend Project Structure
app/
├── api/
│   ├── auth.py        # Login & Registration APIs
│   ├── notes.py       # Notes CRUD APIs
│   └── versions.py    # Note versioning APIs
│
├── core/
│   ├── config.py      # Environment configuration
│   └── security.py   # JWT & password utilities
│
├── db/
│   ├── base.py        # SQLAlchemy Base
│   ├── session.py    # Database session
│   └── init_db.py    # Table initialization
│
├── models/
│   └── user.py       # User ORM model
│
├── schemas/
│   └── user.py       # Pydantic schemas
│
└── main.py            # Application entry point

📂 Frontend Project Structure
pages/
├── index.js           # Login page
├── register.js        # Registration page
├── notes.js           # Notes dashboard
│
lib/
└── api.js             # Centralized API handler

🔐 Authentication Flow (Detailed)
Registration

Endpoint: POST /auth/register

Input: email, password

Password is hashed

User saved to database

Returns user ID and email

Login

Endpoint: POST /auth/login

Input: email, password

Password verified

JWT token generated

Token returned to frontend

Protected Requests

Token sent as:

Authorization: Bearer <token>


Backend extracts user ID

User validated before action

🔗 API Endpoints
Auth
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login and get token
Notes
Method	Endpoint	Description
POST	/notes	Create a note
GET	/notes	Get user notes
🧪 Running Locally
Backend Setup
git clone https://github.com/arshithaManaf7034/notes-api.git
cd notes-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend Setup
git clone https://github.com/arshithaManaf7034/notes-frontend.git
cd notes-frontend
npm install
npm run dev

🌱 Environment Variables
Backend .env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

Frontend .env.local
NEXT_PUBLIC_API_URL=https://notes-api-f8qj.onrender.com

🧠 Major Challenges Solved

✅ JWT authentication & user context

✅ CORS issues with Vercel dynamic URLs

✅ Database table initialization

✅ Response validation errors

✅ Frontend crash due to empty JSON

✅ Secure token handling

✅ Full cloud deployment

📌 Future Enhancements

🎨 Modern UI (cards, animations)

🌙 Dark mode

🗂 Note categories & tags

🕒 Note version comparison

🔍 Search notes

👤 User profile page

👩‍💻 Author

Arshitha KM
Full-Stack Python Developer

GitHub: https://github.com/arshithaManaf7034
