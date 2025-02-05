import sys
import os

# Ensure the backend directory is in the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.db_connection import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
