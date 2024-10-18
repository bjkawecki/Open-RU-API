from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_connection import Base

if TYPE_CHECKING:
    from src.models.word.model_word_db import WordModel


class PropsModel(Base):
    __tablename__ = "props_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped["WordModel"] = relationship(back_populates="props", single_parent=True)
