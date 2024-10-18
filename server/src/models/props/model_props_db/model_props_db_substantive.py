from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship
from src.models.props.model_props_base import PropsBase

if TYPE_CHECKING:
    from src.models.word.model_word_db import Word


class Genus(str, Enum):
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTRAL = "neutral"
    NONE = "none"


class DeclinationClass(str, Enum):
    CLS1 = "1"
    CLS2 = "2"
    CLS3 = "3"
    CLS4 = "adjective"
    CLS5 = "irregular"
    CLS6 = "none"


class Stress(str, Enum):
    ROOT = "root"
    SUFFIX = "suffix"
    SHIFTING = "shifting"


class SubstantiveProps(PropsBase, table=True):
    is_alive: bool
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="substantive_props_obj",
    )
    genus: Genus
    declination_class: DeclinationClass
    stress: Stress
    is_animate: bool = False
    is_singular_tantum: bool = False
    is_plural_tantum: bool = False

    singular_nominative: str | None
    singular_genitive: str | None
    singular_dative: str | None
    singular_accusative: str | None
    singular_instrumental: str | None
    singular_prepositive: str | None

    plural_nominative: str | None
    plural_genitive: str | None
    plural_dative: str | None
    plural_accusative: str | None
    plural_instrumental: str | None
    plural_prepositive: str | None

    partitive: str | None
    locative: str | None
