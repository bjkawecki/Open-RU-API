from typing import List

from fastapi import APIRouter, Depends, HTTPException
from src.db_connection import Session, get_session
from src.enums.word import WordClass
from src.models.props_adjective import AdjectivePropsModel
from src.models.props_substantive import SubstantivePropsModel
from src.models.translation import TranslationModel
from src.models.word import WordModel
from src.schema.word import WordCreateSchema, WordPublicSchema

router = APIRouter(tags=["Wörter"])


@router.post("/words/", response_model=WordPublicSchema)
async def create_word(
    req_body: WordCreateSchema, session: Session = Depends(get_session)
):
    db_obj = WordModel(
        name=req_body.name,
        name_accent=req_body.name_accent,
        word_class=req_body.word_class,
        comment=req_body.comment,
        usage=req_body.usage,
        origin=req_body.origin,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)

    for translation in req_body.translations:
        new_translation_obj = TranslationModel(name=translation.name, word_id=db_obj.id)
        session.add(new_translation_obj)

    if req_body.props:
        props_obj = {}
        props = req_body.props.dict()
        if db_obj.word_class == WordClass.adjective:
            props_obj = AdjectivePropsModel(**props, word_id=db_obj.id)
        elif db_obj.word_class == WordClass.substantive:
            props_obj = SubstantivePropsModel(**props, word_id=db_obj.id)
        session.add(props_obj)

    session.commit()
    session.refresh(db_obj)
    return db_obj


@router.delete("/words/")
async def delete_words(session: Session = Depends(get_session)):
    words = session.query(WordModel).all()
    for word in words:
        session.delete(word)
    session.commit()
    return {"message": "Words successfully deleted."}


@router.get(
    "/words/",
    response_model_exclude_none=True,
    response_model=List[WordPublicSchema],
)
async def read_words(session: Session = Depends(get_session)):
    return session.query(WordModel).all()


@router.get(
    "/words/{word_id}",
    response_model_exclude_none=True,
    response_model=WordPublicSchema,
)
async def get_word_details(word_id: int, session: Session = Depends(get_session)):
    word = session.get(WordModel, word_id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word with ID {word_id} not found.")
    return word
