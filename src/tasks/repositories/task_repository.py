from src.tasks.models.task_model import TaskModel
from sqlalchemy.orm import Session


# Repository layer is used to handle all database operations separately from business logic.

# @staticmethod is used when method functionality is logically related to the class but does not require
#  access to instance variables (self) or class variables (cls). In enterprise applications, it is 
# commonly used in utility classes and repository layers for reusable stateless operations.

# Repository Layer
# Handles all database operations


class TaskRepository:

    # create task
    @staticmethod
    def create_task_repository(body, db: Session, user):

        # convert schema into dictionary
        data = body.model_dump()

        # create task object
        new_task = TaskModel(

            title=data["title"],

            description=data["description"],

            is_completed=data["is_completed"],

            user_id=user.id
        )

        # add object into database session
        db.add(new_task)

        # commit transaction
        db.commit()

        # refresh latest values
        db.refresh(new_task)

        return new_task


    # get all tasks
    @staticmethod
    def get_tasks_repository(db: Session, user):

        return db.query(TaskModel).filter(
            TaskModel.user_id == user.id
        ).all()


    # get task by id
    @staticmethod
    def get_task_by_id_repository(task_id: int, db: Session):

        return db.query(TaskModel).get(task_id)


    # update task
    @staticmethod
    def update_task_repository(tasks, body, db: Session):

        # convert schema into dictionary
        body = body.model_dump()

        # dynamically update fields
        for field, value in body.items():

            setattr(tasks, field, value)

        # save changes
        db.add(tasks)

        db.commit()

        db.refresh(tasks)

        return tasks


    # delete task
    @staticmethod
    def delete_task_repository(tasks, db: Session):

        db.delete(tasks)

        db.commit()

        return None


    # pagination
    @staticmethod
    def get_tasks_pagination_repository(
        page: int,
        limit: int,
        db: Session
    ):

        # calculate skip records
        skip = (page - 1) * limit

        # total records
        total_records = db.query(TaskModel).count()

        # fetch paginated records
        tasks = (
            db.query(TaskModel)
            .offset(skip)
            .limit(limit)
            .all()
        )

        return {
            "page": page,
            "limit": limit,
            "total_records": total_records,
            "data": tasks
        }