from src.tasks.models.task_model import TaskModel
from sqlalchemy.orm import Session
from src.user.models import UserModel
from fastapi import HTTPException, status
from src.tasks.schemas.task_schema import TaskSchema
from src.tasks.repositories.task_repository import TaskRepository

# Service class is used to separate business logic from controllers/routers

# service layer
def create_task_service(body, db, user):

    # return response
    return TaskRepository.create_task_repository(body, db, user)

# get task service
def get_tasks_service(db, user):

    return TaskRepository.get_tasks_repository(db, user)

# tasks get by id
def get_task_by_id(task_id:int, db: Session, user: UserModel):
    
    return TaskRepository.get_task_by_id_repository(task_id, db)

# tasks update
def update_task(body:TaskSchema,task_id:int, db: Session, user: UserModel):
    

    return TaskRepository.update_task_repository(body, task_id, db)

# delete tasks
def delete_task(task_id:int, db: Session, user: UserModel):
    

    return TaskRepository.delete_task_repository(task_id, db)

# Pagination logic for fetching tasks
def get_tasks_pagination(page: int, limit: int, db: Session):

    # Response
    return TaskRepository.get_tasks_pagination_repository(page, limit, db)