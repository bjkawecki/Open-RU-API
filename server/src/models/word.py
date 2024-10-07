import enum
from sqlmodel import SQLModel, Field, Column, Enum, Relationship


class Origin(enum.Enum):
    German = "German"
    English = "English"
    French = "French"
    Turkish = "Turkish"
    Persian = "Persian"
    Dutch = "Dutch"
    Arabian = "Arabian"
    Italian = "Italian"
    Latin = "Latin"
    Greek = "Greek"
    Slavonic = "Church Slavonic"


class Usage(enum.Enum):
    sophisticated = "sophisticated"
    colloquial = "colloquial"
    formal = "formal"
    mat = "mat"
    archaic = "archaic"
    poetic = "poetic"
    term = "term"
    abbreviation = "abbreviation"


class WordClass(enum.Enum):
    adjective = "adjective"
    adverb = "adverb"
    compound = "compound"
    conjunction = "conjunction"
    interjection = "interjection"
    numeral = "numeral"
    particle = "particle"
    phrase = "phrase"
    preposition = "preposition"
    pronoun = "pronoun"
    substantive = "substantive"
    verb = "verb"


class TranslationBase(SQLModel):
    name: str
    word_id: int | None = Field(default=None, foreign_key="word.id", nullable=False)


class Translation(TranslationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    word: "Word" = Relationship(back_populates="translations")


class WordBase(SQLModel):

    name: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    name_accent: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    word_class: WordClass = Field(sa_column=Column(Enum(WordClass)))
    comment: str | None = Field(None, nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage)))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin)))


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
    translations: list[Translation] = Relationship(back_populates="word", cascade_delete=True)


class WordCreate(WordBase):
    translations: list[Translation]


class TranslationPublic(TranslationBase):
    id: int


class TranslationWithWord(TranslationPublic):
    word: Word | None = None


class WordPublic(WordBase):
    id: int


class WordWithTranslations(WordPublic):
    translations: list[Translation] | None = None
