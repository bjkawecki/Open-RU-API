from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship
from src.models.props.model_props_base import PropsBase

if TYPE_CHECKING:
    from src.models.word.model_word_db import Word


class PrepositionType(str, Enum):
    LOCAL = "local"
    DIRECTIONAL = "directional"
    TEMPORAL = "temporal"
    CAUSAL = "causal"
    MODAL = "modal"


class PreopsitionCase(str, Enum):
    GENITIVE = "genitive"
    DATIVE = "dative"
    ACCUSATIVE = "accusative"
    INSTRUMENTAL = "instrumental"
    PREPOSITIVE = "prepositive"


class PrepositionProps(PropsBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="preposition_props_obj",
    )
    preposition_type: PrepositionType
    preposition_case: PreopsitionCase
