from typing import Literal, Optional

from pydantic import BaseModel
from src.enums.props import PreopsitionCase, PrepositionType


class PrepositionPropsBaseSchema(BaseModel):
    preposition_case: Optional[PreopsitionCase] = None
    preposition_type: Optional[PrepositionType] = None


class PrepositionPropsCreateSchema(PrepositionPropsBaseSchema):
    props_type: Literal["preposition"]
