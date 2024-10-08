from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING

from src.models.props.props_base import WordPropsBase

if TYPE_CHECKING:
    from src.models.word.word_db import Word


class WordProps(WordPropsBase):
    pass


class AdjectiveProps(WordProps, table=True):
    id: int = Field(default=None, primary_key=True)
    is_gradable: bool
    word: "Word" = Relationship(sa_relationship_kwargs={"uselist": False}, back_populates="props")
