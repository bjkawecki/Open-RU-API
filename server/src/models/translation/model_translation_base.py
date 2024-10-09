from sqlmodel import SQLModel, Field


class TranslationBase(SQLModel):
    name: str
    word_id: int = Field(default=None, foreign_key="word.id", nullable=False)
