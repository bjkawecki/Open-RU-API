from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from src.db_connection import get_session
from src.models.translation.model_translation_db import Translation
from src.models.translation.model_translation_public import TranslationWithWord

router = APIRouter(tags=["Übersetzungen"])


@router.delete("/translations/")
async def delete_all_translations(session: Session = Depends(get_session)):
    translation_list = session.exec(select(Translation)).all()
    for translation in translation_list:
        session.delete(translation)
        session.commit()
    return {"message": "Translations successfully deleted."}


@router.get("/translations/", response_model=list[TranslationWithWord])
async def get_translation(session: Session = Depends(get_session)):
    translation_list = session.exec(select(Translation)).all()
    return translation_list
