from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from src.db_connection import get_session
from src.models.word.model_word_db import Word

router = APIRouter(tags=["Wörter"])


@router.delete("/words/")
async def delete_words(session: Session = Depends(get_session)):
    words = session.exec(select(Word)).all()
    for word in words:
        session.delete(word)
    session.commit()
    return {"message": "Words successfully deleted."}
