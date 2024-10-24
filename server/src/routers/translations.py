from fastapi import APIRouter, Depends
from src.db_connection import Session, get_session
from src.models.translation import Translation
from src.schema.translation import TranslationPublicSchema

router = APIRouter(tags=["Übersetzungen"])


@router.get(
    "/translations/", response_model=list[TranslationPublicSchema], status_code=200
)
async def get_translation(session: Session = Depends(get_session)):
    return session.query(Translation).all()
