from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_connection import Base

if TYPE_CHECKING:
    from src.models.word.model_word_db import WordModel


class TranslationModel(Base):
    __tablename__ = "translation_table"

    id: Mapped[int] = mapped_column(default=None, primary_key=True)
    name: Mapped[str]
    word_id: Mapped[int] = mapped_column(ForeignKey("word_table.id"))
    word: Mapped["WordModel"] = relationship(back_populates="translations")
