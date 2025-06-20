import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.integrations.database_client import create_database_tables

if __name__ == "__main__":
    print("Initializing database...")
    create_database_tables()
    print("Database initialized successfully.")
