from sqlmodel import SQLModel, Field


class WordPropsBase(SQLModel):
    word_id: int | None = Field(default=None, foreign_key="word.id", nullable=False)
