from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.props_base import Props


class AdjectiveProps(Props):
    __tablename__ = "adjective_props_table"

    id: Mapped[int] = mapped_column(ForeignKey("props_table.id"), primary_key=True)

    is_gradable: Mapped[bool] = mapped_column(default=True)

    masculine_nominative: Mapped[Optional[str]]
    masculine_genitive: Mapped[Optional[str]]
    masculine_dative: Mapped[Optional[str]]
    masculine_accusative: Mapped[Optional[str]]
    masculine_instrumental: Mapped[Optional[str]]
    masculine_prepositive: Mapped[Optional[str]]

    feminine_nominative: Mapped[Optional[str]]
    feminine_genitive: Mapped[Optional[str]]
    feminine_dative: Mapped[Optional[str]]
    feminine_accusative: Mapped[Optional[str]]
    feminine_instrumental: Mapped[Optional[str]]
    feminine_prepositive: Mapped[Optional[str]]

    neutral_nominative: Mapped[Optional[str]]
    neutral_genitive: Mapped[Optional[str]]
    neutral_dative: Mapped[Optional[str]]
    neutral_accusative: Mapped[Optional[str]]
    neutral_instrumental: Mapped[Optional[str]]
    neutral_prepositive: Mapped[Optional[str]]

    plural_nominative: Mapped[Optional[str]]
    plural_genitive: Mapped[Optional[str]]
    plural_dative: Mapped[Optional[str]]
    plural_accusative: Mapped[Optional[str]]
    plural_instrumental: Mapped[Optional[str]]
    plural_prepositive: Mapped[Optional[str]]

    shortform_masculine: Mapped[Optional[str]]
    shortform_feminine: Mapped[Optional[str]]
    shortform_neutral: Mapped[Optional[str]]
    shortform_plural: Mapped[Optional[str]]

    comparative: Mapped[Optional[str]]
    superlative: Mapped[Optional[str]]

    __mapper_args__ = {
        "polymorphic_identity": "adjective",
    }
