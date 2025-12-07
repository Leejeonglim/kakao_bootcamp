# app/routes/post_routes.py
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..schemas.post_schema import PostCreate, PostRead
from ..controllers import post_controller

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.get("/", response_model=List[PostRead])
def list_posts(db: Session = Depends(get_db)):
    return post_controller.list_posts(db)


@router.get("/{post_id}", response_model=PostRead)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_controller.get_post(post_id, db)


@router.post("/", response_model=PostRead, status_code=201)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_controller.create_post(post, db)


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_controller.delete_post(post_id, db)
    return
