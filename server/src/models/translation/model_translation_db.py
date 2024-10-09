from sqlmodel import Field, Relationship
from src.models.word.model_word_db import Word
from src.models.translation.model_translation_base import TranslationBase


class Translation(TranslationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: Word = Relationship(back_populates="translations")
