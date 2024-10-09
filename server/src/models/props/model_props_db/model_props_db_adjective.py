from sqlmodel import Field, Relationship
from typing import TYPE_CHECKING
from src.models.props.model_props_base import PropsBase

if TYPE_CHECKING:
    from src.models.word.model_word_db import Word


class AdjectiveProps(PropsBase, table=True):
    is_gradable: bool
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(sa_relationship_kwargs={"uselist": False}, back_populates="adjective_props")
