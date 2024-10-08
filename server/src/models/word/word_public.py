from src.models.word.word_base import WordBase
from src.models.translation.translation_db import Translation


class WordPublic(WordBase):
    id: int


class WordWithTranslations(WordPublic):
    translations: list[Translation] | None = None
