from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING

from src.models.word.model_word_base import WordBase
from src.models.props.model_props_db.model_props_db_adjective import AdjectiveProps
from src.models.props.model_props_db.model_props_db_substantive import SubstantiveProps

if TYPE_CHECKING:
    from src.models.translation.model_translation_db import Translation


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    translation_list: list["Translation"] = Relationship(back_populates="word", cascade_delete=True)
    adjective_props_obj: AdjectiveProps | None = Relationship(back_populates="word", cascade_delete=True)
    substantive_props_obj: SubstantiveProps | None = Relationship(back_populates="word", cascade_delete=True)
