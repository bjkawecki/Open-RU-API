from fastapi import APIRouter, Depends
from src.db_connection import Session, get_session
from src.models.props_adjective import AdjectivePropsModel
from src.models.props_substantive import SubstantivePropsModel
from src.models.translation import TranslationModel
from src.models.word import WordModel
from src.schema.word import WordBaseSchema, WordCreateSchema, WordPublicSchema

router = APIRouter(tags=["Wörter"])


def add_props(sent_word_data: WordCreateSchema, new_word_obj: WordPublicSchema):
    if new_word_obj.word_class == "adjective":
        return AdjectivePropsModel(
            **sent_word_data.props.dict(), word_id=new_word_obj.id
        )

    elif (
        new_word_obj.word_class == "substantive"
        and sent_word_data.substantive_props_obj
    ):
        return SubstantivePropsModel(
            **sent_word_data.substantive_props_obj.dict(), word_id=new_word_obj.id
        )


@router.post("/words/", response_model=WordPublicSchema)
async def create_word(
    sent_word_data: WordCreateSchema, session: Session = Depends(get_session)
):
    new_word_obj = WordModel(
        name=sent_word_data.name,
        name_accent=sent_word_data.name_accent,
        word_class=sent_word_data.word_class,
        comment=sent_word_data.comment,
        usage=sent_word_data.usage,
        origin=sent_word_data.origin,
    )
    session.add(new_word_obj)
    session.commit()
    session.refresh(new_word_obj)

    for translation in sent_word_data.translations:
        new_translation_obj = TranslationModel(
            name=translation.name, word_id=new_word_obj.id
        )
        session.add(new_translation_obj)

    props_obj = add_props(sent_word_data=sent_word_data, new_word_obj=new_word_obj)
    if props_obj:
        session.add(props_obj)

    session.commit()
    session.refresh(new_word_obj)
    return new_word_obj
