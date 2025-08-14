from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Post
from app.database import SessionLocal, engine, Base
from app.schemas import PostCreate, Post as PostSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts", response_model=list[PostSchema])
def read_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()

@app.post("/posts", response_model=PostSchema)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post