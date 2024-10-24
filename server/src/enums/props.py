from enum import Enum


class NumeralType(str, Enum):
    cardinal = "cardinal"
    collecting = "collecting"
    ordinal = "ordinal"


class PrepositionType(str, Enum):
    local = "local"
    directional = "directional"
    temporal = "temporal"
    causal = "causal"
    modal = "modal"


class PreopsitionCase(str, Enum):
    genitive = "genitive"
    dative = "dative"
    accusative = "accusative"
    instrumental = "instrumental"
    prepositive = "prepositive"


class PronounType(str, Enum):
    persoial = "personal"
    possessive = "possessive"
    demonstrative = "demonstrative"
    interrogative = "interrogative"
    relative = "relative"
    definite = "definite"
    indefinite = "indefinite"
    negation = "negation"


class DeclinationType(str, Enum):
    adjective = "adjective"
    substantive = "substantive"
    none = "none"


class Genus(str, Enum):
    masculine = "masculine"
    feminine = "feminine"
    neutral = "neutral"
    none = "none"


class DeclinationClass(str, Enum):
    class_1 = "1"
    class_2 = "2"
    class_3 = "3"
    adjective = "adjective"
    irregular = "irregular"
    none = "none"


class Stress(str, Enum):
    root = "root"
    suffix = "suffix"
    shifting = "shifting"


class Aspect(str, Enum):
    perfective = "perfective"
    imperfective = "imperfective"
    dual = "dual"


class ConjugationClass(str, Enum):
    e = "e"
    i = "i"
    irregular = "irregular"


class Direction(str, Enum):
    unidirectional = "unidirectional"
    multidirectional = "multidirectional"


class ObjectCase(str, Enum):
    genitive = "genitive"
    dative = "dative"
    accusative = "accusative"
    instrumental = "instrumental"
    prepositive = "prepositive"
