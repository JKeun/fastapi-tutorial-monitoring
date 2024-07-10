from fastapi import FastAPI, Depends

from core import models
from core.base import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get("/api/")
def root():
    return {"message": "This is a backend side API section."}


@app.get("/api/users")
def get_users(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    # db의 User table에서 [skip: limit] 까지의 리스트
    return db.query(models.User).offset(skip).limit(limit).all()


@app.get("/api/createuser")
def create_user(username: str, password: str, email: str, db = Depends(get_db)):  # 나중에 User Create 객체로 받아오도록 수정
    # User 객체 생성
    db_user = models.User(username=username, password=password, email=email)
    # db에 추가
    db.add(db_user)
    # db에 반영
    db.commit()
    # db에 추가된 객체 반환
    db.refresh(db_user)
    return db_user
    