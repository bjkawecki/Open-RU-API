from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from src.db_connection import Session, get_session
from src.models.word import WordModel

# from src.models.word.model_word_public import WordPublic

router = APIRouter(tags=["Wörter"])


# @router.get(
#     "/words/", response_model=list[WordPublic], response_model_exclude_none=True
# )
# async def get_words_with_translation_list(session: Session = Depends(get_session)):
#     word_list = session.exec(select(WordModel)).all()
#     return word_list


# @router.get(
#     "/words/{word_id}", response_model=WordPublic, response_model_exclude_none=True
# )
# async def get_word_details(
#     word_id: int, session: Session = Depends(get_session)
# ) -> WordModel:
#     word = session.get(WordModel, word_id)
#     if word is None:
#         raise HTTPException(status_code=404, detail="Word with ID {word_id} not found.")
#     return word
