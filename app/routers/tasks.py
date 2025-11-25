from fastapi import APIRouter, HTTPException, Depends #type: ignore
from app.schemas.tasks import TaskCreate
from sqlalchemy.orm import Session #type: ignore
from app.db.database import get_db
from app.models.tasks import Task

router = APIRouter()

@router.post("/tasks/")
async def create_task(task : TaskCreate, db: Session=Depends(get_db)):
    nuevo = Task(name=task.name, description=task.description) #definimos los valores que se van a almacenar en memoria
    db.add(nuevo) #guardamos en memoria
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/tasks/")
async def read_tasks(db: Session = Depends(get_db)):
    tareas= db.query(Task).all()
    return tareas

@router.get("/tasks/{task_id}")
async def read_task(task_id: int, db: Session = Depends(get_db)):
    tarea = db.query(Task).filter(Task.id == task_id).first()
    if not tarea:
        raise HTTPException(status_code=404, detail="tarea no encontrada")
    else:
        return tarea

@router.put("/tasks/{task_id}")
async def update_task(task_id:int, task:TaskCreate, db: Session=Depends(get_db)): #la logica al llamar a task(schema) es que ahi van los datos a actualizar
    tarea_db= db.query(Task).filter(Task.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")
    else:
        tarea_db.name = task.name
        tarea_db.description = task.description
        db.commit()
        db.refresh(tarea_db)
        return tarea_db


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    tarea_db = db.query(Task).filter(Task.id == task_id).first()
    if not tarea_db:
        raise HTTPException(status_code=404, detail="tarea no encontrada")
    else:
        db.delete(tarea_db)
        db.commit()
        return {"message": f"La tarea eliminada fue {task_id}"}

