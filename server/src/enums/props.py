from enum import Enum


class NumeralType(str, Enum):
    CARDINAL = "cardinal"
    COLLECTING = "collecting"
    ORDINAL = "ordinal"


class PrepositionType(str, Enum):
    LOCAL = "local"
    DIRECTIONAL = "directional"
    TEMPORAL = "temporal"
    CAUSAL = "causal"
    MODAL = "modal"


class PreopsitionCase(str, Enum):
    GENITIVE = "genitive"
    DATIVE = "dative"
    ACCUSATIVE = "accusative"
    INSTRUMENTAL = "instrumental"
    PREPOSITIVE = "prepositive"


class PronounType(str, Enum):
    PERSONAL = "personal"
    POSSESSIVE = "possessive"
    DEMONSTRATIVE = "demonstrative"
    INTERROGATIVE = "interrogative"
    RELATIVE = "relative"
    DEFINITE = "definite"
    INDEFINITE = "indefinite"
    NEGATION = "negation"


class DeclinationType(str, Enum):
    ADJECTIVE = "adjective"
    SUBSTANTIVE = "substantive"
    NO = "no"


class Genus(str, Enum):
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTRAL = "neutral"
    NONE = "none"


class DeclinationClass(str, Enum):
    CLS1 = "1"
    CLS2 = "2"
    CLS3 = "3"
    CLS4 = "adjective"
    CLS5 = "irregular"
    CLS6 = "none"


class Stress(str, Enum):
    ROOT = "root"
    SUFFIX = "suffix"
    SHIFTING = "shifting"


class Aspect(str, Enum):
    PERFECTIVE = "perfective"
    IMPERFECTIVE = "imperfective"
    DUAL = "dual"


class ConjugationClass(str, Enum):
    E_CONJUGATION = "e"
    I_CONJUGATION = "i"
    IRREGULAR = "irregular"


class Direction(str, Enum):
    UNIDIRECTIONAL = "unidirectional"
    MULTIDIRECTIONAL = "multidirectional"


class ObjectCase(str, Enum):
    GENITIVE = "genitive"
    DATIVE = "dative"
    ACCUSATIVE = "accusative"
    INSTRUMENTAL = "instrumental"
    PREPOSITIVE = "prepositive"
