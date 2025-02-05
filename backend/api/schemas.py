from pydantic import BaseModel
from typing import List, Optional

class TaskBase(BaseModel):
    name: str
    status: Optional[str] = "pending"

class TaskCreate(TaskBase):
    project_id: int

class Task(TaskBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True

class TaskDependencyBase(BaseModel):
    task_id: int
    depends_on_task_id: int

class TaskDependency(TaskDependencyBase):
    id: int

    class Config:
        from_attributes = True
