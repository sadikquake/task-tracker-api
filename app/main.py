from fastapi import FastAPI
from app.routers import tasks
from alembic.config import Config
from alembic import command

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

run_migrations()

app = FastAPI()
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"status": "ok"}