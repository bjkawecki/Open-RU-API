from sqlmodel import Column, Enum, Field, SQLModel
from src.models.word.model_word_enums import Origin, Usage, WordClass


class WordBase(SQLModel):
    name: str = Field(
        nullable=False,
        schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f.,!?]+$"},
    )
    name_accent: str = Field(
        nullable=False,
        schema_extra={
            "pattern": r"^[\u0401\u0451\u0410-\u044f.,!?А́Е́И́О́У́Ы́Э́Ю́Я́áéи́óу́ы́э́я́ю́]+$"
        },
    )
    word_class: WordClass
    comment: str | None = Field(None, nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage)))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin)))
