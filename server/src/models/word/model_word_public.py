from src.models.word.model_word_base import WordBase
from src.models.translation.model_translation_db import Translation
from src.models.props.model_props_db.model_props_db_adjective import AdjectiveProps
from src.models.props.model_props_db.model_props_db_substantive import SubstantiveProps


class WordPublic(WordBase):
    id: int
    translation_list: list[Translation] | None = None
    adjective_props_obj: AdjectiveProps | None = None
    substantive_props_obj: SubstantiveProps | None = None
