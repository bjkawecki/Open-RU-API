from fastapi import Depends, APIRouter
from sqlmodel import Session, select

from src.models.word import Translation, TranslationWithWord
from src.db import get_session

router = APIRouter(tags=["Übersetzungen"])


@router.delete("/translations/")
async def delete_translations(session: Session = Depends(get_session)):
    translations = session.exec(select(Translation)).all()
    for translation in translations:
        session.delete(translation)
        session.commit()
    return {"message": "Translations successfully deleted."}


@router.get("/translations/", response_model=list[TranslationWithWord])
async def get_translation(session: Session = Depends(get_session)):
    translation_list = session.exec(select(Translation)).all()
    return translation_list
