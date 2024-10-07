from fastapi import FastAPI, Depends, Path, HTTPException
from typing import List, Annotated
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware

from src.models.word import Word, WordBase
from src.db import get_session


app = FastAPI()

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
    words = session.exec(select(Word)).all()
    return words


@app.get("/words/{word_id}")
async def get_word_details(
    word_id: Annotated[int, Path(title="Word ID")], session: Session = Depends(get_session)
) -> Word:
    word = session.get(Word, word_id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word not found.")
    return word


@app.delete("/words/")
async def delete_words(session: Session = Depends(get_session)):
    words = session.exec(select(Word)).all()
    for word in words:
        session.delete(word)
        session.commit()
    return {"message": "Words successfully deleted."}
