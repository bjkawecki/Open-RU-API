from fastapi import Depends, APIRouter
from sqlmodel import Session

from src.db import get_session
from src.models.word.model_word_db import Word
from src.models.translation.model_translation_db import Translation
from src.models.word.model_word_create import WordCreate
from src.models.word.model_word_public import WordPublic
from src.models.props.model_props_db.model_props_db_adjective import AdjectiveProps
from src.models.props.model_props_db.model_props_db_substantive import SubstantiveProps

router = APIRouter(tags=["Wörter"])


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

    if word.word_class == "adjective" and word_data.adjective_props:
        props_obj = AdjectiveProps(**word_data.adjective_props.dict(), word=word)
        session.add(props_obj)
    elif word.word_class == "substantive" and word_data.substantive_props:
        props_obj = SubstantiveProps(**word_data.substantive_props.dict(), word=word)
        session.add(props_obj)

    session.commit()
    session.refresh(word)
    return word
