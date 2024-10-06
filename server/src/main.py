from fastapi import FastAPI, Depends
from typing import List
from contextlib import asynccontextmanager
from db import init_db, get_session
import uvicorn
import sys
from models import Word, WordBase
from sqlmodel import Session

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

origins = ["http://localhost:3000", "http://localhost:8000", "http://172.20.0.3:3000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/words/", response_model=Word)
async def create_word(word_data: WordBase, session: Session = Depends(get_session)) -> Word:
    word = Word(**word_data.dict())
    session.add(word)
    session.commit()
    session.refresh(word)
    return word


@app.get("/")
async def get_index() -> str:
    return "Welcome to Open Ru API"


@app.get("/words/", response_model=List[Word])
async def get_words(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    words = session.query(Word).offset(skip).limit(limit).all()
    return words


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("server:app", host="0.0.0.0", port=3001)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
