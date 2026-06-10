# task-tracker-api

A simple REST API for managing tasks, built with FastAPI and PostgreSQL. Supports full CRUD operations and runs entirely in Docker.

## Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.11 |
| Framework | FastAPI |
| Database | PostgreSQL 15 |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Containers | Docker + Docker Compose |

## Getting Started

### Prerequisites
- Docker Desktop installed and running

### Run the project

```bash
git clone https://github.com/sadikquake/task-tracker-api.git
cd task-tracker-api
cp .env.example .env
docker compose up --build
```

API will be available at `http://localhost:8000`  
Interactive docs (Swagger UI) at `http://localhost:8000/docs`

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task by ID |
| DELETE | `/tasks/{id}` | Delete a task by ID |

### Example request

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

### Example response

```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "is_done": false,
  "created_at": "2026-06-10T12:30:04.184169"
}
```

## Environment Variables

Copy `.env.example` to `.env` before running:

```
DATABASE_URL=postgresql://user:password@db:5432/taskdb
```

## Project Structure

```
task-tracker-api/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database connection
│   └── routers/
│       └── tasks.py     # CRUD endpoints
├── alembic/             # Database migrations
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── .env.example
```
