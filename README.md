# 💸 Expense Tracker API

A modern, scalable **RESTful Expense Tracker API** built with **FastAPI** and **Python**, following a clean, modular, and production-inspired architecture.

This project is part of my backend development journey, where I'm focusing on building real-world backend applications while learning API design, request validation, service-oriented architecture, and scalable software engineering practices.

> **Project Status:** 🚧 Actively under development. New backend features, an Analytics Layer, and an AI Layer will be added as the project evolves.

---

# 🚀 Features

- ➕ Create new expenses
- 📋 Retrieve all expenses
- 🔍 Retrieve a single expense by ID
- ✅ Request validation using Pydantic
- 🚦 Proper HTTP status codes
- ⚠️ Structured error handling with FastAPI's HTTPException
- 🧱 Layered architecture (Routes → Services → Data Layer)
- 📖 Interactive API documentation with Swagger UI
- 🧩 Clean and modular project structure
- 📝 Type hints for better readability and maintainability

---

# 🏗️ Architecture

```
                Client
                   │
                   ▼
        Routes (API Layer)
                   │
                   ▼
     Services (Business Logic)
                   │
                   ▼
       Database / Storage Layer
```

Each layer has a single responsibility, making the application easier to maintain, test, and extend.

---

# 📂 Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── expenses.py
│   │
│   └── services/
│       ├── __init__.py
│       └── expense_service.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- REST API
- Virtual Environment (venv)
- Git
- GitHub

---

# ⚡ Getting Started

## 1. Clone the repository

```bash
git clone git@github.com:gaurav123-hue/expense-tracker-api.git
```

## 2. Navigate to the project

```bash
cd expense-tracker-api
```

## 3. Create and activate a virtual environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the application

```bash
uvicorn app.main:app --reload
```

---

# 📖 API Documentation

After starting the server, visit:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📚 Current API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| GET | `/about` | Project information |
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses/{expense_id}` | Retrieve a specific expense |

---

# 🎯 What I Learned

While building this project, I gained practical experience with:

- Designing RESTful APIs
- FastAPI routing and project organization
- Request validation using Pydantic
- HTTP methods and status codes
- Exception handling
- Layered backend architecture
- Separation of concerns
- Service-oriented design
- Type annotations
- Building maintainable backend applications
- Git & GitHub workflow

---

# 🔮 Roadmap

This project is actively being improved and will continue to evolve with additional backend features.

## 🔧 Backend

- [ ] Update Expense API
- [ ] Delete Expense API
- [ ] Filtering and Searching
- [ ] Pagination
- [ ] Sorting
- [ ] Better ID generation
- [ ] SQLite Integration
- [ ] SQLAlchemy ORM
- [ ] PostgreSQL
- [ ] JWT Authentication
- [ ] User Accounts
- [ ] Role-Based Authorization
- [ ] Docker Support
- [ ] Automated Testing
- [ ] CI/CD Pipeline

---

## 📊 Analytics Layer

Planned analytics features include:

- Spending insights
- Category-wise analytics
- Monthly & yearly reports
- Trend analysis
- Financial dashboards
- Expense statistics
- Data visualization endpoints

---

## 🤖 AI Layer

The long-term goal is to integrate AI capabilities into the application, including:

- AI-powered expense categorization
- Smart spending insights
- Personalized saving recommendations
- Budget prediction and forecasting
- Natural language expense entry
- AI-generated financial summaries
- Conversational AI assistant for expense management

---

# 🌱 Project Status

🚧 **This project is actively under development.**

I'm continuously improving the architecture while learning modern backend development. New features, better design patterns, database integration, analytics capabilities, and AI-powered functionality will be added over time.

---

# 🤝 Contributing

Contributions, suggestions, and feedback are always welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

# 👨‍💻 Author

**Gaurav Parpol**

GitHub: https://github.com/gaurav123-hue

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

It helps support the project and motivates future development.
