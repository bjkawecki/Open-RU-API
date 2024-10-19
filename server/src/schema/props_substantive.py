from typing import Literal, Optional

from pydantic import BaseModel
from src.schema.enums.props import DeclinationClass, Genus, Stress


class SubstantivePropsBaseSchema(BaseModel, use_enum_values=True):
    props_type: Literal["substantive"]

    genus: Genus
    declination_class: DeclinationClass
    stress: Stress

    is_alive: Optional[bool] = None
    is_singular_tantum: Optional[bool] = None
    is_plural_tantum: Optional[bool] = None

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

    partitive: Optional[str] = None
    locative: Optional[str] = None


class SubstantivePropsCreateSchema(SubstantivePropsBaseSchema):
    id: int
