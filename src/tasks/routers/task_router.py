from fastapi import APIRouter, Depends, status
from src.tasks.controllers import task_controller
from src.tasks.schemas.task_schema import TaskSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel

# Router layer is used to define API endpoints and map HTTP requests to application logic

# Creates a separate router for task-related APIs
# prefix="/tasks" automatically adds '/tasks' before all task endpoints
# examples: http://127.0.0.1:8000/tasks/create
task_router = APIRouter(prefix="/tasks")

# insert tasks
@task_router.post("/create",response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body: TaskSchema, db:Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return task_controller.create_task(body, db, user)

# get all tasks
@task_router.get("/all_task", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_task( db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return task_controller.get_tasks(db,user)

# tasks update by id 
@task_router.get("/get_task_by_id/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return task_controller.get_task_by_id(task_id, db,user)

# tasks update
@task_router.put("/update_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(body:TaskSchema, task_id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return task_controller.update_task(body, task_id, db,user)

# delete tasks
@task_router.delete("/delete_task/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return task_controller.delete_task(task_id, db,user)

# get_tasks_by_pagination
@task_router.get("/get_tasks_by_pagination")
def get_all_tasks(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return task_controller.get_tasks_pagination(page, limit, db)