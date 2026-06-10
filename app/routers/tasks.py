from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.post("/tasks", response_model=TaskResponse)
def post_task(task: TaskCreate, db: Session = Depends(get_db)):
    task = Task(**task.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    task_item = db.query(Task).filter(Task.id == task_id).first()
    if not task_item:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        for field, value in task.model_dump(exclude_unset=True).items():
            setattr(task_item, field, value)
        db.commit()
        db.refresh(task_item)
    return task_item

@router.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task_item = db.query(Task).filter(Task.id == task_id).first()
    if not task_item:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        db.delete(task_item)
        db.commit()
    return {"message": f"Task id {task_id} was deleted!"}