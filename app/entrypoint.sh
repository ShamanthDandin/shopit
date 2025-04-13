#!/bin/sh


wait-for-it postgres:5432 -t 60

python database.py


exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
