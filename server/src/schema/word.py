from typing import List, Optional, Union

from pydantic import BaseModel, Field
from src.schema.enums.word import Origin, Usage, WordClass
from src.schema.props_adjective import AdjectivePropsBaseSchema
from src.schema.props_substantive import SubstantivePropsBaseSchema
from src.schema.translation import TranslationBaseSchema


class WordBaseSchema(BaseModel, use_enum_values=True):
    model_config = {"extra": "forbid"}
    name: str = Field(pattern=r"^[\u0401\u0451\u0410-\u044f.,!?]+$")
    name_accent: str = Field(
        pattern=r"^[\u0401\u0451\u0410-\u044f.,!?А́Е́И́О́У́Ы́Э́Ю́Я́áéи́óу́ы́э́я́ю́]+$"
    )
    word_class: WordClass
    comment: Optional[str] = None
    origin: Optional[Origin] = None
    usage: Optional[Usage] = None


class WordCreateSchema(WordBaseSchema, use_enum_values=True):
    translations: List[TranslationBaseSchema]
    props: Optional[Union[AdjectivePropsBaseSchema, SubstantivePropsBaseSchema]] = (
        Field(discriminator="props_type")
    )


class WordPublicSchema(WordCreateSchema):
    id: int
