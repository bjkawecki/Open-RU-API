from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.db_connection import get_session
from src.models.word.model_word_db import Word
from src.models.word.model_word_public import WordPublic

router = APIRouter(tags=["Wörter"])


@router.get(
    "/words/", response_model=list[WordPublic], response_model_exclude_none=True
)
async def get_words_with_translation_list(session: Session = Depends(get_session)):
    word_list = session.exec(select(Word)).all()
    return word_list


@router.get(
    "/words/{word_id}", response_model=WordPublic, response_model_exclude_none=True
)
async def get_word_details(
    word_id: int, session: Session = Depends(get_session)
) -> Word:
    word = session.get(Word, word_id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word with ID {word_id} not found.")
    return word
