from pydantic import BaseModel


class TranslationBaseSchema(BaseModel):
    name: str


class TranslationPublicSchema(BaseModel):
    name: str
    word_id: int
