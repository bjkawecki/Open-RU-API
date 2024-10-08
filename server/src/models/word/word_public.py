from src.models.word.word_base import WordBase
from src.models.translation.translation_db import Translation
from src.models.props.props_db import AdjectiveProps


class WordPublic(WordBase):
    id: int
    translations: list[Translation] | None = None
    props: AdjectiveProps | None = None
