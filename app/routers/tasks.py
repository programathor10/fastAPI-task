from fastapi import APIRouter, HTTPException, Depends #type: ignore
from sqlalchemy.orm import Session #type: ignore
from typing import List

from app.db.database import get_db
from app.schemas.tasks import TaskCreate, Task
from app.models.tasks import Task as TaskModel

router = APIRouter()

# CREATE
@router.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    nuevo = TaskModel(name=task.name, description=task.description)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# READ ALL
@router.get("/tasks/", response_model=List[Task])
async def read_tasks(db: Session = Depends(get_db)):
    tareas = db.query(TaskModel).all()
    return tareas

# READ ONE
@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int, db: Session = Depends(get_db)):
    tarea = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="tarea no encontrada")
    return tarea

# UPDATE
@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    tarea_db = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")

    tarea_db.name = task.name
    tarea_db.description = task.description

    db.commit()
    db.refresh(tarea_db)
    return tarea_db

# DELETE
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    tarea_db = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")

    db.delete(tarea_db)
    db.commit()
    return {"message": f"La tarea eliminada fue {task_id}"}

