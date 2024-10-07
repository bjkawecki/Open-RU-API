import enum
from sqlmodel import SQLModel, Field, Column, Enum


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


class WordBase(SQLModel):

    name: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    name_accent: str = Field(nullable=False, schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"})
    word_class: WordClass = Field(sa_column=Column(Enum(WordClass)))
    comment: str = Field(nullable=True)
    usage: Usage | None = Field(None, sa_column=Column(Enum(Usage), nullable=True))
    origin: Origin | None = Field(None, sa_column=Column(Enum(Origin), nullable=True))


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
