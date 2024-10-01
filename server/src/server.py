from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
import uvicorn
import sys

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000", "http://localhost:8000", "http://172.20.0.3:3000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WordBase(BaseModel):
    name: str
    name_accent: str
    comment: str
    usage: str
    origin: str


class WordModel(WordBase):
    id: int

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


@app.post("/words/", response_model=WordModel)
async def create_word(word: WordBase, db: db_dependency):
    db_word = models.Word(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word


@app.get("/words/", response_model=List[WordModel])
async def get_words(db: db_dependency, skip: int = 0, limit: int = 100):
    words = db.query(models.Word).offset(skip).limit(limit).all()
    return words


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
