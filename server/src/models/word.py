from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_connection import Base
from src.enums.word import Origin, Usage, WordClass
from src.models.props.base import PropsModel
from src.models.translation import TranslationModel


class WordModel(Base):
    __tablename__ = "word_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    unique_name: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    name_accent: Mapped[str]
    word_class: Mapped[WordClass]

    comment: Mapped[Optional[str]]

    usage: Mapped[Optional[Usage]]
    origin: Mapped[Optional[Origin]]

    props: Mapped[Optional["PropsModel"]] = relationship(back_populates="props")
    translations: Mapped[list["TranslationModel"]] = relationship(back_populates="word")
