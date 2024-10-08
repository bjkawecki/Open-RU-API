from sqlmodel import SQLModel, Field, Column, Enum, Relationship

from src.models.enums import Origin, Usage, WordClass


class WordBase(SQLModel):

    name: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    name_accent: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    word_class: WordClass = Field(sa_column=Column(Enum(WordClass)))
    comment: str | None = Field(None, nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage)))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin)))


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    translations: list["Translation"] = Relationship(back_populates="word", cascade_delete=True)


class WordCreate(WordBase):
    translations: list["Translation"]


class WordPublic(WordBase):
    id: int


class WordWithTranslations(WordPublic):
    translations: list["Translation"] | None = None


class TranslationBase(SQLModel):
    name: str
    word_id: int | None = Field(default=None, foreign_key="word.id", nullable=False)


class Translation(TranslationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: Word = Relationship(back_populates="translations")


class TranslationPublic(TranslationBase):
    id: int


class TranslationWithWord(TranslationPublic):
    word: Word | None = None
