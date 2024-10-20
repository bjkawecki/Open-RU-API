from enum import Enum


class Origin(str, Enum):
    german = "German"
    english = "English"
    french = "French"
    turkish = "Turkish"
    persian = "Persian"
    dutch = "Dutch"
    arabian = "Arabian"
    italian = "Italian"
    latin = "Latin"
    greek = "Greek"
    slavonic = "Church Slavonic"


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