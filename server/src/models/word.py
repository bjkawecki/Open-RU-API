from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_connection import Base
from src.enums.word import Origin, Usage, WordClass
from src.models.props_base import Props
from src.models.translation import Translation


class Word(Base):
    __tablename__ = "word_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    # unique_name: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    name_accent: Mapped[str]
    word_class: Mapped[WordClass]

    comment: Mapped[Optional[str]]

    usage: Mapped[Optional[Usage]]
    origin: Mapped[Optional[Origin]]

    props: Mapped[Optional["Props"]] = relationship(
        back_populates="word", cascade="all, delete-orphan"
    )

    translations: Mapped[Optional[list["Translation"]]] = relationship(
        back_populates="word", cascade="all, delete-orphan"
    )
