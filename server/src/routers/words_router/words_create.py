from fastapi import Depends, APIRouter
from sqlmodel import Session, select

from src.db import get_session
from src.models.word.model_word_db import Word
from src.models.translation.model_translation_db import Translation
from src.models.word.model_word_create import WordCreate
from src.models.word.model_word_public import WordPublic
from src.models.props.model_props_db.model_props_db_adjective import AdjectiveProps

router = APIRouter(tags=["Wörter"])


@router.get("/words/", response_model=list[WordPublic], response_model_exclude_none=True)
async def get_words_with_translations(session: Session = Depends(get_session)):
    word_list = session.exec(select(Word)).all()
    return word_list


@router.post("/words/", response_model=WordPublic, response_model_exclude_none=True)
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
    if word_data.adjective_props:
        props_obj = AdjectiveProps(is_gradable=word_data.props.is_gradable, word=word)
        session.add(props_obj)
    session.commit()
    session.refresh(word)
    return word
