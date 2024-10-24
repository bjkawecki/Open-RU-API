import re
from typing import List, Optional, Union

from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError
from src.enums.word import Level, Origin, Usage, WordClass
from src.schema.props_adjective import AdjectivePropsCreateSchema
from src.schema.props_numeral import NumeralPropsCreateSchema
from src.schema.props_preposition import PrepositionPropsCreateSchema
from src.schema.props_pronoun import PronounPropsCreateSchema
from src.schema.props_substantive import SubstantivePropsCreateSchema
from src.schema.props_verb import VerbPropsCreateSchema
from src.schema.translation import TranslationBaseSchema
from src.validators.word import Pattern


def has_valid_pattern(*, pattern: str, input_value: str) -> bool:
    match = re.match(pattern, input_value)
    return bool(match)


class WordBaseSchema(BaseModel, use_enum_values=True):
    model_config = {"extra": "forbid"}
    name: str
    name_accent: str
    word_class: WordClass
    comment: Optional[str] = None
    origin: Optional[Origin] = None
    usage: Optional[Usage] = None
    topic: Optional[str] = None
    level: Optional[Level] = None

    @field_validator("name")
    def validate_name(cls, input_value: str) -> str:
        if not has_valid_pattern(pattern=Pattern.name, input_value=input_value):
            raise PydanticCustomError(
                "string_pattern_mismatch",
                f"Word name '{input_value}' doesn't match. Only cyrillic letters.",
                {"name": input_value},
            )

        return input_value


class WordCreateSchema(WordBaseSchema):
    translations: List[TranslationBaseSchema]
    props: Optional[
        Union[
            AdjectivePropsCreateSchema,
            NumeralPropsCreateSchema,
            PrepositionPropsCreateSchema,
            PronounPropsCreateSchema,
            SubstantivePropsCreateSchema,
            VerbPropsCreateSchema,
        ]
    ] = Field(discriminator="props_type")


class WordPublicSchema(WordCreateSchema):
    id: int


class WordMetaSchema(BaseModel):
    level: str
    topic: str


class WordClassSchema(BaseModel):
    name: WordClass
