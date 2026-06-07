from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings  import settings

# Creates base class for all SQLAlchemy database models/tables
Base = declarative_base()

# Creates database engine/connection using PostgreSQL connection URL
engine = create_engine(url=settings.DB_CONNECTION)

# Creates local database session factory for handling DB operations
LocalSession = sessionmaker(bind=engine)

# Dependency function for getting database session in FastAPI APIs
def get_db():

    # Creates new database session/connection
    session = LocalSession()

    try:
        # Provides session to API/request
        yield session

    finally:
        # Closes database session after request completion
        session.close()
