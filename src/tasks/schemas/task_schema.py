# dtos: data transfer objects

from pydantic import BaseModel

# Request schema used for creating/updating task data from API request body
class TaskSchema(BaseModel):
    title : str
    description : str
    is_completed : bool = False

# Response schema used for sending task data back to client
class TaskResponseSchema(BaseModel):
    id : int
    title : str
    description : str
    is_completed : bool
     # Associated user id (optional)
    user_id : int | None = 0