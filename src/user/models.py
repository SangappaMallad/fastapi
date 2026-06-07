from sqlalchemy import Column, String, Integer
from src.utils.db import Base

# UserModel represents user_table in PostgreSQL database
class UserModel(Base):
    # Database table name
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    userName = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String)

