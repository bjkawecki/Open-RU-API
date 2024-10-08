from src.models.base_models import TranslationBase, WordBase
from src.models.db_models import Word, Translation


class WordPublic(WordBase):
    id: int


class WordWithTranslations(WordPublic):
    translations: list[Translation] | None = None


class TranslationPublic(TranslationBase):
    id: int


class TranslationWithWord(TranslationPublic):
    word: Word | None = None
