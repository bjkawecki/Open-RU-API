from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.db_connection import get_session
from src.models.props.model_props_db.model_props_db_adjective import AdjectiveProps
from src.models.props.model_props_db.model_props_db_substantive import SubstantiveProps
from src.models.translation.model_translation_db import Translation
from src.models.word.model_word_create import WordCreate
from src.models.word.model_word_db import Word
from src.models.word.model_word_public import WordPublic

router = APIRouter(tags=["Wörter"])


def add_translation(sent_word_data: WordCreate, new_word_obj: Word) -> Translation:
    for translation in sent_word_data.translation_list:
        return Translation(name=translation.name, word=new_word_obj)


def add_props(sent_word_data: WordCreate, new_word_obj: Word):
    if new_word_obj.word_class == "adjective" and sent_word_data.adjective_props_obj:
        return AdjectiveProps(
            **sent_word_data.adjective_props_obj.dict(), word=new_word_obj
        )

    elif (
        new_word_obj.word_class == "substantive"
        and sent_word_data.substantive_props_obj
    ):
        return SubstantiveProps(
            **sent_word_data.substantive_props_obj.dict(), word=new_word_obj
        )


@router.post("/words/", response_model=WordPublic, response_model_exclude_none=True)
async def create_word(
    sent_word_data: WordCreate, session: Session = Depends(get_session)
) -> Word:
    new_word_obj = Word(
        name=sent_word_data.name,
        name_accent=sent_word_data.name_accent,
        word_class=sent_word_data.word_class,
        comment=sent_word_data.comment,
        usage=sent_word_data.usage,
        origin=sent_word_data.origin,
    )
    session.add(new_word_obj)
    translation_obj = add_translation(
        sent_word_data=sent_word_data, new_word_obj=new_word_obj
    )
    session.add(translation_obj)
    props_obj = add_props(sent_word_data=sent_word_data, new_word_obj=new_word_obj)
    if props_obj:
        session.add(props_obj)
    session.commit()
    session.refresh(new_word_obj)
    return new_word_obj
