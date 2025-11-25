from fastapi import FastAPI #type: ignore
from app.routers.tasks import router
from app.db.database import engine, Base
from app.models import tasks as models

app = FastAPI(title="Task CRUD")

app.include_router(router)

Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "API de Tasks funcionando"}

