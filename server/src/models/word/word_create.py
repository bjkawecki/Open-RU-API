from src.models.word.word_base import WordBase
from src.models.translation.translation_db import Translation
from src.models.props.props_db import AdjectiveProps


class WordCreate(WordBase):
    translations: list[Translation]
    props: AdjectiveProps
