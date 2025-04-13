#!/bin/sh

# Wait for the database to be ready
wait-for-it postgres:5432 -t 60

# Run database migrations or table creation
python database.py

# Start the FastAPI application
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
