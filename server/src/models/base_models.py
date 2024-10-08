from sqlmodel import SQLModel, Field, Column, Enum

from src.models.enums import Origin, Usage, WordClass


class WordBase(SQLModel):

    name: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    name_accent: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    word_class: WordClass = Field(sa_column=Column(Enum(WordClass)))
    comment: str | None = Field(None, nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage)))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin)))


class TranslationBase(SQLModel):
    name: str
    word_id: int | None = Field(default=None, foreign_key="word.id", nullable=False)
