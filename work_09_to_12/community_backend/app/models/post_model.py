# app/models/post_model.py
from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import Session

from ..db import Base
from ..schemas.post_schema import PostCreate


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


# ---------- CRUD 함수 ----------

def get_all_posts(db: Session) -> List[Post]:
    return db.query(Post).order_by(Post.id.desc()).all()


def get_post_by_id(db: Session, post_id: int) -> Optional[Post]:
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, data: PostCreate) -> Post:
    post = Post(
        title=data.title,
        content=data.content,
        author=data.author,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post_id: int) -> bool:
    post = get_post_by_id(db, post_id)
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True
