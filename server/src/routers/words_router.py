from fastapi import Depends, Path, HTTPException, APIRouter
from typing import Annotated
from sqlmodel import Session, select

from src.db import get_session
from src.models.word_model import Word, WordCreate, Translation, WordWithTranslations

router = APIRouter(tags=["Wörter"])


@router.get("/words/", response_model=list[WordWithTranslations])
async def get_words_with_translations(session: Session = Depends(get_session)):
    word_list = session.exec(select(Word)).all()
    return word_list


@router.post("/words/", response_model=Word)
async def create_word(word_data: WordCreate, session: Session = Depends(get_session)) -> Word:
    word = Word(
        name=word_data.name,
        name_accent=word_data.name_accent,
        word_class=word_data.word_class,
        comment=word_data.comment,
        usage=word_data.usage,
        origin=word_data.origin,
    )
    session.add(word)
    if word_data.translations:
        for translation in word_data.translations:
            translation_obj = Translation(name=translation.name, word=word)
            session.add(translation_obj)
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
