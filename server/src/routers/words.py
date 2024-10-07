from fastapi import Depends, Path, HTTPException, APIRouter
from typing import List, Annotated
from sqlmodel import Session, select

from src.models.word import Word, WordBase
from src.db import get_session

router = APIRouter(tags=["Wörter"])


@router.get("/words/", response_model=List[Word])
async def get_words(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    words = session.exec(select(Word)).all()
    return words


@router.post("/words/", response_model=Word)
async def create_word(word_data: WordBase, session: Session = Depends(get_session)) -> Word:
    word = Word(**word_data.dict())
    session.add(word)
    session.commit()
    session.refresh(word)
    return word


@router.delete("/words/")
async def delete_words(session: Session = Depends(get_session)):
    words = session.exec(select(Word)).all()
    for word in words:
        session.delete(word)
        session.commit()
    return {"message": "Words successfully deleted."}


@router.get("/words/{word_id}")
async def get_word_details(
    word_id: Annotated[int, Path(title="Word ID")], session: Session = Depends(get_session)
) -> Word:
    word = session.get(Word, word_id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word not found.")
    return word
