from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from src.utils.db import Base

# TaskModel represents user_tasks table in PostgreSQL database
class TaskModel(Base):
    # Database table name
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)

    # Foreign key column linked with user_table.id
    # ondelete="CASCADE" automatically deletes user tasks if user is deleted
    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))

    