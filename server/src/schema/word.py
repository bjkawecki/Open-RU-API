from pydantic import BaseModel, Field
from src.enums.word import Origin, Usage, WordClass


class WordBase(BaseModel, use_enum_values=True):
    model_config = {"extra": "forbid"}
    name: str = Field(pattern=r"^[\u0401\u0451\u0410-\u044f.,!?]+$")
    name_accent: str = Field(
        pattern=r"^[\u0401\u0451\u0410-\u044f.,!?А́Е́И́О́У́Ы́Э́Ю́Я́áéи́óу́ы́э́я́ю́]+$"
    )
    word_class: WordClass
    comment: str | None
    origin: Origin | None
    usage: Usage | None
    # translation_list: list[Translation]
    # adjective_props_obj: AdjectiveProps | None = None
    # substantive_props_obj: SubstantiveProps | None = None
