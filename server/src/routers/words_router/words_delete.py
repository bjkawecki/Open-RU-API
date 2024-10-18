from fastapi import APIRouter, Depends
from sqlalchemy import select
from src.db_connection import Session, get_session
from src.models.word import WordModel

router = APIRouter(tags=["Wörter"])


@router.delete("/words/")
async def delete_words(session: Session = Depends(get_session)):
    words = session.exec(select(WordModel)).all()
    for word in words:
        session.delete(word)
    session.commit()
    return {"message": "Words successfully deleted."}
