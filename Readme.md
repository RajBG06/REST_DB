# User Data API

A FastAPI application that fetches user data from JSONPlaceholder API and stores it in a SQLite database.

## Features

- Fetches user data from external API (JSONPlaceholder)
- Stores data in SQLite database (easily configurable to use PostgreSQL)
- RESTful API endpoints
- Automatic OpenAPI documentation
- Data validation using Pydantic
- ORM using SQLAlchemy

## Project Structure

```
rest_db/
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── config.py          # Configuration settings
├── database.py        # Database connection setup
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── services.py        # Business logic
└── main.py           # FastAPI application
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository or create a new directory:
```bash
mkdir rest_db
cd rest_db
```

2. Create and activate a virtual environment:

On Unix/macOS:
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Create the required files and install dependencies:
```bash
# Create requirements.txt
echo "fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
requests==2.31.0
python-dotenv==1.0.0
pydantic==2.5.1
pydantic-settings==2.1.0" > requirements.txt

# Install dependencies
pip install -r requirements.txt
```

4. Create a `.env` file:
```bash
echo "DATABASE_URL=sqlite:///./users.db
API_URL=https://jsonplaceholder.typicode.com/users" > .env
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

2. The API will be available at:
- Main API: http://127.0.0.1:8000
- API Documentation: http://127.0.0.1:8000/docs

## API Endpoints

1. Test if API is running:
```bash
curl http://127.0.0.1:8000/
```

2. Sync users from external API:
```bash
curl -X POST http://127.0.0.1:8000/api/sync-users
```

3. Get all users from database:
```bash
curl http://127.0.0.1:8000/api/users
```

## Database

By default, the application uses SQLite. The database file (`users.db`) will be created automatically in your project directory when you first run the application.

### Switching to PostgreSQL

To use PostgreSQL instead of SQLite:

1. Install PostgreSQL database
2. Update the DATABASE_URL in your `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```
3. Install psycopg2:
```bash
pip install psycopg2-binary
```

## Troubleshooting

1. If the port is already in use, try a different port:
```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

2. Check if the server is running:
```bash
curl http://127.0.0.1:8000/
```

3. Verify virtual environment is activated:
- You should see `(venv)` at the start of your command prompt
- If not, activate it using the commands in the Installation section

4. Database issues:
- Check if the database file exists: `ls users.db`
- Verify file permissions: `ls -l users.db`
- Try removing and letting it recreate: `rm users.db`

## API Response Examples

1. Root endpoint (`/`):
```json
{
    "message": "API is running"
}
```

2. Sync users (`/api/sync-users`):
```json
{
    "message": "Users synced successfully",
    "count": 10
}
```

3. Get users (`/api/users`):
```json
[
    {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz",
        "username": "Bret",
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "created_at": "2023-11-22T10:30:00.000Z"
    },
    ...
]
```