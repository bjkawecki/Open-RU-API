import enum


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
