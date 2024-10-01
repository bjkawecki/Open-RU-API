from database import Base
from sqlalchemy import Column, Integer, String


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    name_accent = Column(String)
    comment = Column(String)
    usage = Column(String)
    origin = Column(String)
