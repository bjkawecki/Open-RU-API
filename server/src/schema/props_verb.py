from typing import Literal, Optional

from pydantic import BaseModel
from src.enums.props import Aspect, ConjugationClass, Direction, ObjectCase


class VerbPropsBaseSchema(BaseModel):
    conjugation_class: ConjugationClass
    is_reflexive: Optional[bool] = False
    has_irregular_conjugation: Optional[bool] = False

    aspect: Aspect
    aspect_partner: Optional[str] = None

    is_motion_verb: Optional[bool] = False
    motion_partner: Optional[str] = None
    direction: Optional[Direction] = None

    direct_object_case: Optional[ObjectCase] = None
    direct_object_preposition: Optional[str] = None
    indirect_object_preposition: Optional[str] = None

    present_singular_1: Optional[str] = None
    present_singular_2: Optional[str] = None
    present_singular_3: Optional[str] = None
    present_plural_1: Optional[str] = None
    present_plural_2: Optional[str] = None
    present_plural_3: Optional[str] = None

    future_singular_1: Optional[str] = None
    future_singular_2: Optional[str] = None
    future_singular_3: Optional[str] = None
    future_plural_1: Optional[str] = None
    future_plural_2: Optional[str] = None
    future_plural_3: Optional[str] = None

    past_masculine: Optional[str] = None
    past_feminine: Optional[str] = None
    past_neutral: Optional[str] = None
    past_plural: Optional[str] = None

    participle_active_present: Optional[str] = None
    participle_active_past: Optional[str] = None

    participle_adverbial_present: Optional[str] = None
    participle_adverbial_passive: Optional[str] = None

    participle_passive_present: Optional[str] = None
    participle_passive_past: Optional[str] = None

    imperative_singular: Optional[str] = None
    imperative_plural: Optional[str] = None


class VerbPropsCreateSchema(VerbPropsBaseSchema):
    props_type: Literal["verb"]
