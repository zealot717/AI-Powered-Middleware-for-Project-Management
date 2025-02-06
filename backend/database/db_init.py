from sqlalchemy.orm import Session
from .db_connection import engine, Base

def create_tables():
    """Creates all tables if they don't exist."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
