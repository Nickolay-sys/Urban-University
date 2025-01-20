from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from models import *
from typing import Annotated
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify 

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_user(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no users"
        )
    return users

@router.get("/user_id")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User)).where(User.id == user_id)
    if user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    return user

@router.get("/user_id/tasks")
async def tasks_by_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id))
    return tasks
    
@router.post("/create")
async def create_user(create: CreateUser, db: Annotated[Session, Depends(get_db)]):
    db.execute(insert(User).values(
        username=create.username,
        firstname=create.firstname,
        lastname=create.lastname,
        age=create.age,
        slug=slugify(create.username))
    )
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update")
async def update_user(user_update: UpdateUser, user_id: int, db: Annotated[Session, Depends(get_db)]):
    update_user = db.scalars(select(User).where(User.id == user_id)).first()
    if update_user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    db.execute(update(User).where(User.id == user_id).values(
        firstname=user_update.firstname,
        lastname=user_update.lastname,
        age=user_update.age
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete("/delete")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    delete_user = db.scalars(select(User).where(User.id == user_id)).first()
    if delete_user is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    db.execute(delete(User).where(User.id == user_id))
    db.scalar(select(Task).where(Task.user_id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}