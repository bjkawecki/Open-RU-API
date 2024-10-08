from src.models.word.word_base import WordBase
from src.models.translation.translation_db import Translation


class WordCreate(WordBase):
    translations: list[Translation]
