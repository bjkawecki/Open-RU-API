from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db_connection import Base

if TYPE_CHECKING:
    from src.models.word import WordModel


class PropsModel(Base):
    __tablename__ = "props_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("word_table.id"))
    word: Mapped["WordModel"] = relationship(back_populates="props", single_parent=True)
    props_type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "props",
        "polymorphic_on": "props_type",
    }
