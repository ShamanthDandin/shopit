from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncpg
import os
from contextlib import asynccontextmanager

# Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Database connection pool
pool = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to DB on startup
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)
    yield
    # Close connection on shutdown
    await pool.close()

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Basic health check endpoint
@app.get("/health")
async def health_check():
    async with pool.acquire() as connection:
        return {"status": "healthy", "database": "connected"}
