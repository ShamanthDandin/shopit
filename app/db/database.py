# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
import tenacity
import logging
import psycopg2
import time
from sqlalchemy.exc import OperationalError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

# Check database health before creating tables
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
        return create_engine(DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://"), pool_pre_ping=True)
    except OperationalError as e:
        logger.error(f"Failed to connect to database (sync): {e}")
        raise

engine = create_sync_engine()

# Function to create tables
def create_tables():
    try:
        if check_db_health():
            Base.metadata.create_all(bind=engine)
            logger.info("✅ Tables created/verified successfully")
        else:
            logger.error("❌ Database health check failed, aborting table creation")
    except Exception as e:
        logger.error(f"Failed to create tables: {e}")
        raise

# Call create_tables after defining it
create_tables()
