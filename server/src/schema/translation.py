from typing import List

from pydantic import BaseModel


class TranslationBaseSchema(BaseModel):
    name: str


class TranslationListSchema(BaseModel):
    translations: List


class TranslationPublicSchema(BaseModel):
    name: str
    word_id: int
