from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncpg
import os
import logging
from contextlib import asynccontextmanager
import tenacity
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from auth2.auth import login, signup
from db.models import Base
import time
import psycopg2
from sqlalchemy.exc import OperationalError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

pool = None

# Function to check database health
def check_db_health(max_attempts=5, wait_seconds=5):
    for attempt in range(max_attempts):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            conn.close()
            logger.info("✅ Database is healthy")
            return True
        except OperationalError as e:
            logger.warning(f"Database not ready (attempt {attempt + 1}/{max_attempts}): {e}")
            time.sleep(wait_seconds)
    logger.error("❌ Database health check failed")
    return False

@tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10), stop=tenacity.stop_after_attempt(3))
def create_sync_engine():
    try:
        return create_engine(DATABASE_URL)
    except Exception as e:
        logger.error(f"Failed to connect to database (sync): {e}")
        raise

# Create tables 
if check_db_health():
    try:
        engine = create_sync_engine()
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tables created/verified successfully")
    except Exception as e:
        logger.error(f"Failed to create tables: {e}")
    else:
        logger.info("✅ Table creation completed") #Indicate table creation process completion
else:
    logger.error("❌ Aborting table creation due to database health check failure")
    exit(1)

#db connection with retry
@tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10), stop=tenacity.stop_after_attempt(3))
async def create_pool():
    try:
        return await asyncpg.create_pool(DATABASE_URL)
    except Exception as e:
        logger.error(f"Failed to connect to database (async): {e}")
        raise

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pool
    try:
        pool = await create_pool()
        logger.info("✅ Connected to database (async)")
        yield
    except Exception as e:
        logger.error(f"Failed to connect to database (async): {e}")
        raise
    finally:
        if pool:
            await pool.close()
            logger.info("🔌 Database connection closed (async)")

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



app.post("/signup")(signup)
app.post("/login")(login)


'''
System design what would be the best to use 
for backend and frontend

'''
