from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (SQLite in this case, you can modify it for PostgreSQL, MySQL, etc.)
DATABASE_URL = "sqlite:///./test.db"  # You can change this to a different database

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # SQLite-specific

# Create a sessionmaker to interact with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()

# Dependency to get the DB session (for use in FastAPI routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize the database (Create tables, etc.)
def init_db():
    # Create all tables in the database (if they don't already exist)
    Base.metadata.create_all(bind=engine)
