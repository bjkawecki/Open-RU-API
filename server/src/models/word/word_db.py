from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING

from src.models.word.word_base import WordBase
from src.models.props.props_db import AdjectiveProps

if TYPE_CHECKING:
    from src.models.translation.translation_db import Translation


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    translations: list["Translation"] = Relationship(back_populates="word", cascade_delete=True)
    props: AdjectiveProps | None = Relationship(back_populates="word", cascade_delete=True)
