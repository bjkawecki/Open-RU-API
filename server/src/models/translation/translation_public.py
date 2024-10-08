from src.models.translation.translation_base import TranslationBase
from src.models.word.word_db import Word


class TranslationPublic(TranslationBase):
    id: int


class TranslationWithWord(TranslationPublic):
    word: Word | None = None
