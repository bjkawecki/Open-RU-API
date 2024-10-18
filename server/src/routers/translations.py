from fastapi import Depends
from sqlalchemy import select
from src.db_connection import Session, get_session
from src.models.translation import Translation
from src.routers import translations_router as router
from src.schema.translation import TranslationWithWord


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
