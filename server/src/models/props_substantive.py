from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.enums.props import DeclinationClass, Genus, Stress
from src.models.props_base import PropsModel


class SubstantivePropsModel(PropsModel):
    __tablename__ = "substantive_props_table"

    id: Mapped[int] = mapped_column(ForeignKey("props_table.id"), primary_key=True)

    genus: Mapped[Genus]
    declination_class: Mapped[DeclinationClass]
    stress: Mapped[Stress]

    is_alive: Mapped[bool] = mapped_column(default=False)
    is_singular_tantum: Mapped[bool] = mapped_column(default=False)
    is_plural_tantum: Mapped[bool] = mapped_column(default=False)

    singular_nominative: Mapped[Optional[str]]
    singular_genitive: Mapped[Optional[str]]
    singular_dative: Mapped[Optional[str]]
    singular_accusative: Mapped[Optional[str]]
    singular_instrumental: Mapped[Optional[str]]
    singular_prepositive: Mapped[Optional[str]]

    plural_nominative: Mapped[Optional[str]]
    plural_genitive: Mapped[Optional[str]]
    plural_dative: Mapped[Optional[str]]
    plural_accusative: Mapped[Optional[str]]
    plural_instrumental: Mapped[Optional[str]]
    plural_prepositive: Mapped[Optional[str]]

    partitive: Mapped[Optional[str]]
    locative: Mapped[Optional[str]]

    __mapper_args__ = {
        "polymorphic_identity": "substantive",
    }
