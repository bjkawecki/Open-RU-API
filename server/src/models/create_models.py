from src.models.base_models import WordBase
from src.models.db_models import Translation


class WordCreate(WordBase):
    translations: list[Translation]
