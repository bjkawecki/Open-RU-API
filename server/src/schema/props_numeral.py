from typing import Literal, Optional

from pydantic import BaseModel
from src.enums.props import DeclinationType, NumeralType


class NumeralPropsBaseSchema(BaseModel):
    numeral_type: Optional[NumeralType] = None
    declination_type: Optional[DeclinationType] = None

    masculine_nominative: Optional[str] = None
    masculine_genitive: Optional[str] = None
    masculine_dative: Optional[str] = None
    masculine_accusative: Optional[str] = None
    masculine_instrumental: Optional[str] = None
    masculine_prepositive: Optional[str] = None

    feminine_nominative: Optional[str] = None
    feminine_genitive: Optional[str] = None
    feminine_dative: Optional[str] = None
    feminine_accusative: Optional[str] = None
    feminine_instrumental: Optional[str] = None
    feminine_prepositive: Optional[str] = None

    neutral_nominative: Optional[str] = None
    neutral_genitive: Optional[str] = None
    neutral_dative: Optional[str] = None
    neutral_accusative: Optional[str] = None
    neutral_instrumental: Optional[str] = None
    neutral_prepositive: Optional[str] = None

    singular_nominative: Optional[str] = None
    singular_genitive: Optional[str] = None
    singular_dative: Optional[str] = None
    singular_accusative: Optional[str] = None
    singular_instrumental: Optional[str] = None
    singular_prepositive: Optional[str] = None

    plural_nominative: Optional[str] = None
    plural_genitive: Optional[str] = None
    plural_dative: Optional[str] = None
    plural_accusative: Optional[str] = None
    plural_instrumental: Optional[str] = None
    plural_prepositive: Optional[str] = None


class NumeralPropsPropsCreateSchema(NumeralPropsBaseSchema):
    props_type: Literal["numeral"]
