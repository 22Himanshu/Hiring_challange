from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all models to ensure they are registered with the Base
from src.models import booking, conversation, hotel, user
from src.models.user import Base
from src.utils.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
    pool_size=settings.database_pool_size,
    max_overflow=20,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_database_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Get a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
