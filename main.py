from fastapi import FastAPI
from app.routers.tasks import router

app = FastAPI(title="Task CRUD")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API de Tasks funcionando"}

