from pydantic import BaseModel, Field

#schema que recibo al CREAR una tarea
class TaskCreate(BaseModel):
    name: str = Field(..., min_length=1, title="Titulo de la tarea")
    description: str | None = Field(
        default=None, title="Descripcion opcional"
    )

# Schema que devolvemos al LISTAR o MOSTRAR una tarea
class Task(BaseModel):
    id: int
    name: str
    description: str | None