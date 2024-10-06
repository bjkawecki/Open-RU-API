import enum
from sqlmodel import SQLModel, Field, Column, Enum


class Etymology(enum.Enum):
    GERMAN = "German", "Deutsch"
    ENGLISH = "English", "Englisch"
    FRENCH = "French", "Französisch"
    TURKISH = "Turkish", "Türkisch"
    PERSIAN = "Persian", "Persisch"
    DUTCH = "Dutch", "Niederländisch"
    ARABIAN = "Arabian", "Arabisch"
    ITALIAN = "Italian", "Italienisch"
    LATIN = "Latin", "Latein"
    GREEK = "Greek", "Altgriechisch"
    CHURCH_SLAVONIC = "Church Slavonic", "Kirchenlslawisch"


class Usage(enum.Enum):
    SOPHISTICATED = "sophisticated", "gehoben"
    COLLOQUIAL = "colloquial", "umgangssprachlich"
    FORMAL = "formal", "förmlich"
    MAT = "mat", "Mat"
    ARCHAIC = "archaic", "veraltet"
    POETIC = "poetic", "poetisch"
    TERM = "term", "Fachwort"
    ABRREVIATION = "abbreviation", "Abkürzung"


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

    name: str = Field(
        nullable=False,
        schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"},
    )
    name_accent: str = Field(
        nullable=False,
        schema_extra={"pattern": r"^[\u0401\u0451\u0410-\u044f]+$"},
    )
    word_class: WordClass = Field(sa_column=Column(Enum(WordClass)))
    comment: str = Field(nullable=True)
    usage: str = Field(nullable=True)
    origin: str = Field(nullable=True)


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
