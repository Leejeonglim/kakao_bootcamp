# app/controllers/post_controller.py
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..schemas.post_schema import PostCreate, PostRead
from .. import models
from ..models.post_model import get_all_posts, get_post_by_id, create_post as model_create_post, delete_post as model_delete_post


def list_posts(db: Session) -> List[PostRead]:
    posts = get_all_posts(db)
    return [PostRead.from_orm(p) for p in posts]


def get_post(post_id: int, db: Session) -> PostRead:
    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostRead.from_orm(post)


def create_post(data: PostCreate, db: Session) -> PostRead:
    post = model_create_post(db, data)
    return PostRead.from_orm(post)


def delete_post(post_id: int, db: Session) -> None:
    ok = model_delete_post(db, post_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Post not found")
