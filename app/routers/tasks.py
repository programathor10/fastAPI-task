from fastapi import APIRouter, HTTPException
from app.schemas.tasks import TaskCreate

router = APIRouter()
cont_id = 1
tareas = []

@router.post("/tasks/")
async def create_task(task : TaskCreate):
    global cont_id #utilizamos la variable global(sino nos da error)
    task = {"id": cont_id, "name":task.name, "description": task.description} #definimos los valores que se van a almacenar en memoria
    tareas.append(task) #guardamos en memoria
    cont_id += 1 #aumentamos el id por que no estamos en base de datos
    return task

@router.get("/tasks/")
async def read_tasks():
    return tareas

@router.get("/tasks/{task_id}")
async def read_task(task_id: int):
    for tarea in tareas:
        if tarea["id"] == task_id:
            return tarea
        
    raise HTTPException(status_code=404, detail="tarea no encontrada")

@router.put("/tasks/{task_id}")
async def update_task(task_id:int, task:TaskCreate): #la logica al llamar a task(schema) es que ahi van los datos a actualizar
    for tarea in tareas:
        if tarea["id"] == task_id:
            tarea["name"] = task.name
            tarea["description"] = task.description

            return tarea
    raise HTTPException(status_code=404, detail="tarea no encontrada")

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for tarea in tareas:
        if tarea["id"] == task_id:
            tareas.remove(tarea)
            return tarea

    raise HTTPException(status_code=404, detail="tarea no encontrada")