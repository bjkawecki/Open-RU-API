from sqlmodel import SQLModel, Field, Column, Enum

from src.models.word.model_word_enums import Origin, Usage, WordClass


class WordBase(SQLModel):

    name: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    name_accent: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    word_class: str = Field(sa_column=Column(Enum(WordClass)))
    comment: str | None = Field(None, nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage)))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin)))
