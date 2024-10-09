from src.models.translation.model_translation_base import TranslationBase
from src.models.word.model_word_db import Word


class TranslationPublic(TranslationBase):
    id: int


class TranslationWithWord(TranslationPublic):
    word: Word | None = None
