from src.tasks.schemas.task_schema import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models.task_model import TaskModel
from fastapi import HTTPException, status
from src.user.models import UserModel
from src.tasks.services import task_service

# Controller layer is used to handle request/response flow between routers and services.

# insert tasks
def create_task(body: TaskSchema, db : Session, user: UserModel):
   
    # controller handles request flow
    return task_service.create_task_service(body, db, user)

# get all tasks
def get_tasks(db: Session, user: UserModel):
    
    # controller handles request flow
    return task_service.get_tasks_service(db, user)

# tasks get by id
def get_task_by_id(task_id:int, db: Session, user: UserModel):

    # controller handles request flow
    return task_service.get_task_by_id(task_id,db, user)

# tasks update
def update_task(body:TaskSchema,task_id:int, db: Session, user: UserModel):
 
    # controller handles request flow
    return task_service.update_task(body, task_id, db, user)

# delete tasks
def delete_task(task_id:int, db: Session, user: UserModel):
 
     # controller handles request flow
    return task_service.delete_task(task_id, db, user)


# Pagination logic for fetching tasks
def get_tasks_pagination(page: int, limit: int, db: Session):

    # controller handles request flow
    return task_service.get_tasks_pagination(page, limit, db)
    


