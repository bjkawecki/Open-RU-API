from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.enums.props import PreopsitionCase, PrepositionType
from src.models.props_base import PropsModel


class PrepositionPropsModel(PropsModel):
    __tablename__ = "preposition_props_table"

    id: Mapped[int] = mapped_column(ForeignKey("props_table.id"), primary_key=True)

    preposition_case: Mapped[PreopsitionCase]
    preposition_type: Mapped[PrepositionType]
