from enum import Enum


class Origin(str, Enum):
    GERMAN = "German"
    ENGLISCH = "English"
    FRENCH = "French"
    TURKISH = "Turkish"
    PERSIAN = "Persian"
    DUTCH = "Dutch"
    ARABIAN = "Arabian"
    ITALIAN = "Italian"
    LATIN = "Latin"
    GREEK = "Greek"
    SLAVONIC = "Church Slavonic"


class Usage(str, Enum):
    sophisticated = "sophisticated"
    colloquial = "colloquial"
    formal = "formal"
    mat = "mat"
    archaic = "archaic"
    poetic = "poetic"
    term = "term"
    abbreviation = "abbreviation"


class WordClass(str, Enum):
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
