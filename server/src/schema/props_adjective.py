from typing import Literal, Optional

from pydantic import BaseModel


class AdjectivePropsBaseSchema(BaseModel):
    is_gradable: bool

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

    plural_nominative: Optional[str] = None
    plural_genitive: Optional[str] = None
    plural_dative: Optional[str] = None
    plural_accusative: Optional[str] = None
    plural_instrumental: Optional[str] = None
    plural_prepositive: Optional[str] = None

    shortform_masculine: Optional[str] = None
    shortform_feminine: Optional[str] = None
    shortform_neutral: Optional[str] = None
    shortform_plural: Optional[str] = None

    comparative: Optional[str] = None
    superlative: Optional[str] = None


class AdjectivePropsCreateSchema(AdjectivePropsBaseSchema):
    props_type: Literal["adjective_props"]
