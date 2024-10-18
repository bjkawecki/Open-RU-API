from pydantic import BaseModel


class SubstantivePropsBaseSchema(BaseModel):
    genus: str
    declination_class: str
    stress: str

    is_alive: bool
    is_singular_tantum: bool
    is_plural_tantum: bool

    singular_nominative: str
    singular_genitive: str
    singular_dative: str
    singular_accusative: str
    singular_instrumental: str
    singular_prepositive: str

    plural_nominative: str
    plural_genitive: str
    plural_dative: str
    plural_accusative: str
    plural_instrumental: str
    plural_prepositive: str

    partitive: str
    locative: str
