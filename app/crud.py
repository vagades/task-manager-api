from sqlalchemy.orm import Session

from app import models, schemas


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    new_task = models.Task(
        title=task.title,
        description=task.description,
        is_done=False
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session) -> list[models.Task]:
    return db.query(models.Task).all()


def get_task_by_id(db: Session, task_id: int) -> models.Task | None:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task_id: int, task_data: schemas.TaskUpdate) -> models.Task | None:
    task = get_task_by_id(db, task_id)
    if task is None:
        return None

    task.title = task_data.title
    task.description = task_data.description
    task.is_done = task_data.is_done

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task_by_id(db, task_id)
    if task is None:
        return False

    db.delete(task)
    db.commit()
    return True