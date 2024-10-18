from enum import Enum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship
from src.models.props.model_props_base import PropsBase

if TYPE_CHECKING:
    from src.models.word.model_word_db import Word


class Aspect(str, Enum):
    PERFECTIVE = "perfective"
    IMPERFECTIVE = "imperfective"
    DUAL = "dual"


class ConjugationClass(str, Enum):
    E_CONJUGATION = "e"
    I_CONJUGATION = "i"
    IRREGULAR = "irregular"


class Direction(str, Enum):
    UNIDIRECTIONAL = "unidirectional"
    MULTIDIRECTIONAL = "multidirectional"


class ObjectCase(str, Enum):
    GENITIVE = "genitive"
    DATIVE = "dative"
    ACCUSATIVE = "accusative"
    INSTRUMENTAL = "instrumental"
    PREPOSITIVE = "prepositive"


class VerbProps(PropsBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(
        sa_relationship_kwargs={"uselist": False}, back_populates="verb_props_obj"
    )

    conjugation_class: ConjugationClass
    is_reflexive: bool = False
    has_irregular_conjugation: bool = False

    aspect: Aspect
    aspect_partner: str

    is_motion_verb: bool = False
    motion_partner: str | None
    direction: Direction

    direct_object_case: ObjectCase | None
    direct_object_preposition: str | None
    indirect_object_preposition: str | None

    present_singular_1: str | None
    present_singular_2: str | None
    present_singular_3: str | None
    present_plural_1: str | None
    present_plural_2: str | None
    present_plural_3: str | None

    future_singular_1: str | None
    future_singular_2: str | None
    future_singular_3: str | None
    future_plural_1: str | None
    future_plural_2: str | None
    future_plural_3: str | None

    past_masculine: str
    past_feminine: str
    past_neutral: str
    past_plural: str

    participle_active_present: str | None
    participle_active_past: str | None

    participle_adverbial_present: str | None
    participle_adverbial_passive: str | None

    participle_passive_present: str | None
    participle_passive_past: str | None

    imperative_singular: str
    imperative_plural: str
