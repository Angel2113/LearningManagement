
This is the backend for the Learning Management System, built with FastAPI and SQLAlchemy.

## Running the Application

### Running Locally

To run the application locally, you can use the provided `run.py` script:

```bash
cd /path/to/LearningManagement/backend
python run.py
```

This script adds the backend directory to the Python path, which ensures that imports like `from app.models import Users` work correctly.

Alternatively, you can run the application directly with uvicorn, but you need to make sure the Python path is set correctly:

```bash
cd /path/to/LearningManagement/backend
PYTHONPATH=$PYTHONPATH:$(pwd) uvicorn app.main:app --reload
```

### Running with Docker

To run the application with Docker, use the provided Docker Compose configuration:

```bash
cd /path/to/LearningManagement
docker-compose up
```

## Common Issues

### ModuleNotFoundError: No module named 'app'

If you encounter this error, it means that the Python path is not set correctly. Make sure you're running the application from the correct directory (backend) or use the provided `run.py` script.

## Project Structure

- `app/`: The main application package
  - `models/`: SQLAlchemy models
  - `main.py`: The FastAPI application entry point
  - `database.py`: Database connection setup