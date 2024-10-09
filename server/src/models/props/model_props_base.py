from sqlmodel import SQLModel, Field


class PropsBase(SQLModel):
    word_id: int | None = Field(foreign_key="word.id")
