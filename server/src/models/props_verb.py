from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.enums.props import Aspect, ConjugationClass, Direction, ObjectCase
from src.models.props_base import PropsModel


class VerbPropsModel(PropsModel):
    __tablename__ = "verb_props_table"

    id: Mapped[int] = mapped_column(ForeignKey("props_table.id"), primary_key=True)

    conjugation_class: Mapped[ConjugationClass]
    is_reflexive: Mapped[bool] = mapped_column(default=False)
    has_irregular_conjugation: Mapped[bool] = mapped_column(default=False)

    aspect: Mapped[Aspect]
    aspect_partner: Mapped[Optional[str]]

    is_motion_verb: Mapped[bool] = mapped_column(default=False)
    motion_partner: Mapped[Optional[str]]
    direction: Mapped[Optional[Direction]]

    direct_object_case: Mapped[Optional[ObjectCase]]
    direct_object_preposition: Mapped[Optional[str]]
    indirect_object_preposition: Mapped[Optional[str]]

    present_singular_1: Mapped[Optional[str]]
    present_singular_2: Mapped[Optional[str]]
    present_singular_3: Mapped[Optional[str]]
    present_plural_1: Mapped[Optional[str]]
    present_plural_2: Mapped[Optional[str]]
    present_plural_3: Mapped[Optional[str]]

    future_singular_1: Mapped[Optional[str]]
    future_singular_2: Mapped[Optional[str]]
    future_singular_3: Mapped[Optional[str]]
    future_plural_1: Mapped[Optional[str]]
    future_plural_2: Mapped[Optional[str]]
    future_plural_3: Mapped[Optional[str]]

    past_masculine: Mapped[Optional[str]]
    past_feminine: Mapped[Optional[str]]
    past_neutral: Mapped[Optional[str]]
    past_plural: Mapped[Optional[str]]

    participle_active_present: Mapped[Optional[str]]
    participle_active_past: Mapped[Optional[str]]

    participle_adverbial_present: Mapped[Optional[str]]
    participle_adverbial_passive: Mapped[Optional[str]]

    participle_passive_present: Mapped[Optional[str]]
    participle_passive_past: Mapped[Optional[str]]

    imperative_singular: Mapped[Optional[str]]
    imperative_plural: Mapped[Optional[str]]
