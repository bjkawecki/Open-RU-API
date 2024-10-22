import json

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from pydantic import ValidationError
from src.db_connection import Session, get_session
from src.enums.word import WordClass
from src.models.props_adjective import AdjectiveProps
from src.models.props_substantive import SubstantiveProps
from src.models.translation import Translation
from src.models.word import Word
from src.schema.props_adjective import AdjectivePropsBaseSchema
from src.schema.props_substantive import SubstantivePropsBaseSchema
from src.schema.translation import TranslationListSchema
from src.schema.word import WordBaseSchema, WordMetaSchema

router = APIRouter(tags=["Upload"])


@router.post("/file/upload/")
async def upload_file(file: UploadFile, session: Session = Depends(get_session)):
    if not file.content_type == "application/json":
        raise HTTPException(400, detail="Invalid document type.")
    data = json.loads(file.file.read())
    for item in data:
        if not WordBaseSchema.model_validate(item["base"]):
            raise HTTPException(400, detail="Invalid document type: base.")
        if not TranslationListSchema(translations=item["translation"]):
            raise HTTPException(400, detail="Invalid document type: translation.")
        if not WordMetaSchema.model_validate(item["meta"]):
            raise HTTPException(400, detail="Invalid document type: meta")

        base = item["base"]
        translations = item["translation"]
        meta = item["meta"]
        word_class = base["word_class"]
        word_db_obj = Word(**base)
        session.add(word_db_obj)
        session.flush()
        session.refresh(word_db_obj)

        for translation in translations:
            new_translation_obj = Translation(name=translation, word_id=word_db_obj.id)
            session.add(new_translation_obj)

        props = item["props"]

        if word_class == WordClass.adjective:
            try:
                AdjectivePropsBaseSchema.model_validate(props)
                props_obj = AdjectiveProps(**props, word_id=word_db_obj.id)
                session.add(props_obj)
            except ValidationError:
                raise HTTPException(400, detail="Invalid document type: props.")

        elif word_class == WordClass.substantive:
            try:
                SubstantivePropsBaseSchema.model_validate(props)
                props_obj = SubstantiveProps(**props, word_id=word_db_obj.id)
                session.add(props_obj)
            except ValidationError:
                raise HTTPException(400, detail="Invalid document type: props.")

    session.commit()

    return {"result": "success"}