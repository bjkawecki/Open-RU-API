from enum import Enum
from sqlmodel import SQLModel, Field


class WordClass(Enum):
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

    name: str
    name_accent: str
    comment: str
    usage: str
    origin: str


class Word(WordBase, table=True):
    id: int = Field(default=None, primary_key=True)
