from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base  # Ensure models are loaded before table creation

# SQLite database URL
DATABASE_URL = "sqlite:///./aerospace.db"

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# ORM session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Ensure database tables are created."""
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)  # This creates tables properly
    print("Tables created successfully!")
