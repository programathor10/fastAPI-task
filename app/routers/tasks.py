from fastapi import APIRouter, Depends #type: ignore
from sqlalchemy.orm import Session #type: ignore
from typing import List

from app.db.database import get_db
from app.schemas.tasks import TaskCreate, Task
from app.services import tasks_services

router = APIRouter()

# CREATE
@router.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return tasks_services.create_task_service(task,db)

# READ ALL
@router.get("/tasks/", response_model=List[Task])
async def read_tasks(db: Session = Depends(get_db)):
    return tasks_services.read_list_services(db)

# READ ONE
@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    return tasks_services.read_task_service(task_id,db)

# UPDATE
@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return tasks_services.update_task_service(task_id,task,db)

# DELETE
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return tasks_services.delete_task_service(task_id,db)