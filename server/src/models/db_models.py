from sqlmodel import Field, Relationship

from src.models.base_models import WordBase, TranslationBase


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    translations: list["Translation"] = Relationship(back_populates="word", cascade_delete=True)


class Translation(TranslationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: Word = Relationship(back_populates="translations")
