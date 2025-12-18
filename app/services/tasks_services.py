#Este archivo es “el cerebro” de las tareas.
from fastapi import HTTPException #type: ignore 
from sqlalchemy.orm import Session #type: ignore 
from app.models.tasks import Task as TaskModel
from app.schemas.tasks import TaskCreate


def create_task_service(task: TaskCreate, db: Session):
    nuevo = TaskModel(name=task.name, description=task.description)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def read_list_services(db: Session):
    tareas = db.query(TaskModel).all()
    return tareas

def read_task_service(task_id: int,db: Session):
    tarea = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="tarea no encontrada")
    return tarea

def update_task_service(task_id: int,task,db: Session):
    tarea_db = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")

    tarea_db.name = task.name
    tarea_db.description = task.description

    db.commit()
    db.refresh(tarea_db)
    return tarea_db

def delete_task_service(task_id: int,db: Session):
    tarea_db = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")

    db.delete(tarea_db)
    db.commit()
    return {"message": f"La tarea eliminada fue {task_id}"}